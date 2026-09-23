import re

"""
**문제 1.** 입력한 문자열이 **숫자로만** 이루어져 있는지 검사하세요.
- '2026' → 성공, '20a6' → 실패, '' → 실패
"""
print("############## Q1 ##############")

print(re.fullmatch(r'[0-9]+', '2026'))
print(re.fullmatch(r'[0-9]+', '20a6'))

"""
**문제 2.** 문자열이 **대소문자 상관없이 `Python`으로 시작**하는지 검사하세요.
- `'python is easy'` → 성공, `'Learn Python'` → 실패
"""
print("############## Q2 ##############")

print(re.match(r'python', 'python is easy', re.IGNORECASE))

"""
**문제 3.** `010-XXXX-XXXX` 형식(가운데는 숫자 4자리)의 **휴대전화번호**인지 검사하세요.
- `'010-1234-5678'` → 성공, `'010-123-5678'` → 실패, `'010-1234-5678 '` → 실패
"""
print("############## Q3 ##############")

PHONE_PATTERN = re.compile(r'010-[0-9]{4}-[0-9]{4}')
print(PHONE_PATTERN.fullmatch('010-1234-5678'))
print(PHONE_PATTERN.fullmatch('010-123-5678'))
print(PHONE_PATTERN.fullmatch('010-1234-5678 '))

"""
**문제 4.** **한글 이름**(한글 2~4자)인지 검사하세요.
- `'홍길동'` → 성공, `'Hong'` → 실패, `'김'` → 실패
"""
print("############## Q4 ##############")

KOR_NAME_PATTERN = re.compile(r'[가-힣]{2,4}')
print(KOR_NAME_PATTERN.fullmatch('홍길동'))
print(KOR_NAME_PATTERN.fullmatch('Hong'))
print(KOR_NAME_PATTERN.fullmatch('김'))