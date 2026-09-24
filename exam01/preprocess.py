import re
import pandas as pd
from code_maps import CATEGORY_MAPS

FIELDS = ['SYEAR', 'SMONTH', 'SDAY', 'EYEAR', 'EMONTH', 'EDAY', 'SPOT', 'Q6_AR', 'Q6']
# 변수명에서 여행차수, 방문순서, 항목명을 추출합니다.
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

# 코드 열 바로 뒤에 대응하는 명칭 열을 배치합니다.
OUTPUT_COLUMNS = []
for column in code_columns:
    OUTPUT_COLUMNS.append(column)
    if column in CATEGORY_MAPS:
        label, _ = CATEGORY_MAPS[column]
        OUTPUT_COLUMNS.append(label)


def preprocess(df, id_cols, region_map=None, missing_values=None):
    # 원자료를 방문지별 한 행으로 변환하고 분석용 정보를 결합합니다.
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
    # 공백과 빈 값을 정리하고 코드 끝의 소수점 이하 0을 제거합니다.
    values = series.astype('string').str.strip()
    return values.mask(values.eq('')).str.replace(r'\.0+$', '', regex=True)


def validate_input(df, id_cols):
    # 식별 열의 존재 여부와 결측값, 중복을 검사합니다.
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
    # 방문지 변수명을 여행차수와 방문순서별로 묶습니다.
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
    # 사용자가 지정한 결측 코드를 비교 가능한 문자열로 정리합니다.
    rules = {}
    for field, values in (missing_values or {}).items():
        cleaned = normalize_text(pd.Series(values)).dropna()
        rules[field.upper()] = set(cleaned)
    return rules


def extract_visit_rows(source, ids, mapping, missing_rules):
    # 방문 정보가 하나라도 있는 행을 추출하고 필요한 항목을 정리합니다.
    slot = pd.DataFrame({f: normalize_text(source[c]) for f, c in mapping.items()})
    for f, sentinels in missing_rules.items():
        if f in slot:
            slot[f] = slot[f].mask(slot[f].isin(sentinels))
    keep = slot.notna().any(axis=1)
    block = source.loc[keep, ids].copy()
    raw = slot.reindex(columns=FIELDS).loc[keep].astype('string')
    return block, raw


def add_visit_dates(block, raw):
    # 연, 월, 일을 결합하고 유효하지 않은 날짜는 결측값으로 처리합니다.
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
    # 방문, 숙박 지역코드를 보존하고 지역명을 연결합니다.
    result = block.copy()
    for field, label in [('SPOT', '방문지역'), ('Q6_AR', '숙박지역')]:
        result[label + '코드'] = raw[field]
        if region_map is None:
            result[label] = pd.Series(pd.NA, index=result.index, dtype='string')
        else:
            result[label] = raw[field].map(region_map).astype('string')
    return result


def add_trip_fields(block, source, trip):
    # 해당 여행의 유형과 1인 지출비용을 방문 행에 추가합니다.
    result = block.copy()
    for field, label in TRIP_FIELDS.items():
        column = f'D_TRA{trip}_{field}'
        if column in source.columns:
            result[label] = source.loc[block.index, column]
        else:
            result[label] = pd.NA
    return result


def add_respondent_fields(block, source):
    # 응답자의 인구통계 정보를 각 방문 행에 추가합니다.
    result = block.copy()
    for column, label in RESPONDENT_FIELDS.items():
        if column in source.columns:
            result[label] = source.loc[block.index, column]
        else:
            result[label] = pd.NA
    return result


def add_category_names(block):
    # 범주형 코드에 대응하는 명칭 열을 추가합니다.
    result = block.copy()
    for code_column, (label, mapping) in CATEGORY_MAPS.items():
        codes = normalize_text(result[code_column])
        result[label] = codes.map(mapping).astype('string')
    return result


