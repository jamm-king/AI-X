import re
import pandas as pd
from code_maps import CATEGORY_MAPS

FIELDS = ['SYEAR', 'SMONTH', 'SDAY', 'EYEAR', 'EMONTH', 'EDAY', 'SPOT', 'Q6_AR', 'Q6']
PATTERN = re.compile(r'^D_TRA(\d+)_(\d+)_(.+)$', re.IGNORECASE)

TRIP_FIELDS = {
    'CASE': '여행유형코드',
    'ONE_COST': '여행1인지출비용',
}
RESPONDENT_FIELDS = {
    'BSEX': '성별코드',
    'BAGE': '연령대코드',
    'BINC2': '개인소득구간코드',
    'BMAR': '혼인상태코드',
    'BARA': '거주지역코드',
}

code_columns = [
    '여행차수', '방문순서', '방문시작일', '방문종료일',
    '방문지역코드', '숙박지역코드', '방문지역', '숙박지역',
    '숙박시설코드',
] + list(TRIP_FIELDS.values()) + list(RESPONDENT_FIELDS.values())

OUTPUT_COLUMNS = []
for column in code_columns:
    OUTPUT_COLUMNS.append(column)
    if column in CATEGORY_MAPS:
        label, _ = CATEGORY_MAPS[column]
        OUTPUT_COLUMNS.append(label)


def preprocess(df, id_cols, region_map=None, missing_values=None):
    ids = validate_input(df, id_cols)
    groups = group_visit_columns(df.columns)
    missing_rules = normalize_missing_values(missing_values)
    source = df.reset_index(drop=True)
    frames = []

    for (trip, stop), mapping in sorted(groups.items()):
        block, raw = extract_visit_rows(source, ids, mapping, missing_rules)
        if block.empty:
            continue

        block['여행차수'] = trip
        block['방문순서'] = stop
        block = add_visit_dates(block, raw)
        block = add_region_names(block, raw, region_map)
        block['숙박시설코드'] = raw['Q6']
        block = add_trip_fields(block, source, trip)
        block = add_respondent_fields(block, source)
        block = add_category_names(block)
        frames.append(block[ids + OUTPUT_COLUMNS])

    if not frames:
        return pd.DataFrame(columns=ids + OUTPUT_COLUMNS)
    return pd.concat(frames, ignore_index=True)


def normalize_text(series):
    values = series.astype('string').str.strip()
    return values.mask(values.eq('')).str.replace(r'\.0+$', '', regex=True)


def validate_input(df, id_cols):
    ids = [id_cols] if isinstance(id_cols, str) else list(id_cols)
    if not ids or not df.columns.is_unique:
        raise ValueError('식별 열을 지정하고 중복 열 이름을 확인하세요.')
    if any(c not in df.columns for c in ids):
        raise ValueError(f'식별 열이 원자료에 없습니다: {ids}')
    if df[ids].isna().any().any() or any(normalize_text(df[c]).isna().any() for c in ids):
        raise ValueError('식별키에 결측값이 있습니다.')
    if df.duplicated(ids).any():
        raise ValueError('식별키가 중복됩니다. 연도,월 등을 포함한 실제 복합키를 지정하세요.')
    if set(ids) & set(OUTPUT_COLUMNS):
        raise ValueError('식별 열 이름이 결과 열 이름과 겹칩니다.')
    return ids


def group_visit_columns(columns):
    groups = {}
    for col in columns:
        match = PATTERN.fullmatch(str(col))
        if match:
            trip, stop = int(match[1]), int(match[2])
            field = match[3].upper()
            group = groups.setdefault((trip, stop), {})
            if field in group:
                raise ValueError(f'동일 의미의 열이 중복됩니다: {col}')
            group[field] = col
    selected = {}
    for key, mapping in groups.items():
        if set(mapping) & set(FIELDS):
            selected[key] = mapping
    groups = selected
    if not groups:
        raise ValueError('방문지 변수 패턴을 찾지 못했습니다. 원자료 종류와 열 이름을 확인하세요.')
    return groups


def normalize_missing_values(missing_values):
    rules = {}
    for field, values in (missing_values or {}).items():
        cleaned = normalize_text(pd.Series(values)).dropna()
        rules[field.upper()] = set(cleaned)
    return rules


def extract_visit_rows(source, ids, mapping, missing_rules):
    slot = pd.DataFrame({f: normalize_text(source[c]) for f, c in mapping.items()})
    for f, sentinels in missing_rules.items():
        if f in slot:
            slot[f] = slot[f].mask(slot[f].isin(sentinels))
    keep = slot.notna().any(axis=1)
    block = source.loc[keep, ids].copy()
    raw = slot.reindex(columns=FIELDS).loc[keep].astype('string')
    return block, raw


def add_visit_dates(block, raw):
    result = block.copy()
    for prefix, name in [('S', '방문시작일'), ('E', '방문종료일')]:
        fields = [prefix + suffix for suffix in ['YEAR', 'MONTH', 'DAY']]
        parts = raw[fields]
        year = parts.iloc[:, 0].str.zfill(4)
        month = parts.iloc[:, 1].str.zfill(2)
        day = parts.iloc[:, 2].str.zfill(2)
        text = year + '-' + month + '-' + day
        valid_shape = parts.apply(lambda col: col.str.fullmatch(r'\d+', na=False)).all(axis=1)
        result[name] = pd.to_datetime(
            text.where(valid_shape), format='%Y-%m-%d', errors='coerce'
        )
    return result


def add_region_names(block, raw, region_map):
    result = block.copy()
    for field, label in [('SPOT', '방문지역'), ('Q6_AR', '숙박지역')]:
        result[label + '코드'] = raw[field]
        if region_map is None:
            result[label] = pd.Series(pd.NA, index=result.index, dtype='string')
        else:
            result[label] = raw[field].map(region_map).astype('string')
    return result


def add_trip_fields(block, source, trip):
    result = block.copy()
    for field, label in TRIP_FIELDS.items():
        column = f'D_TRA{trip}_{field}'
        if column in source.columns:
            result[label] = source.loc[block.index, column]
        else:
            result[label] = pd.NA
    return result


def add_respondent_fields(block, source):
    result = block.copy()
    for column, label in RESPONDENT_FIELDS.items():
        if column in source.columns:
            result[label] = source.loc[block.index, column]
        else:
            result[label] = pd.NA
    return result


def add_category_names(block):
    result = block.copy()
    for code_column, (label, mapping) in CATEGORY_MAPS.items():
        codes = normalize_text(result[code_column])
        result[label] = codes.map(mapping).astype('string')
    return result


