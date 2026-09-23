import re

m = re.match("hello", "hello world")
print(m)

m = re.match('world', 'hello world')
print(m)

m = re.match(r'[a-z]', 'hel53lo')
print(m)

m = re.match(r'[a-z]+', 'hel53lo')
print(m)

m = re.match(r'[a-z]+$', 'hello1234')
print(m)

m = re.match(r'[0-9]+', '123hello')
print(m)

m = re.match(r'\d+', '123abc')
print(m)

m = re.match(r'\d+', 'abc123')
print(m)

m = re.match(r'\d+', ' 123')
print(m)

m = re.match(r'[가-힣]+', '안녕하세요 Python')
print(m)

m = re.match(r'\d{3}-\d{4}', '333-4444')
print(m)

m = re.match(r'\d{3}-\d{4}', '010-1234-5678')
print(m)

m = re.match('python', 'Python is fun', re.IGNORECASE)
print(m)

m = re.match('python', 'Python is fun')
print(m)

text = '2026년 9월 21일'
if re.match(r'\d{4}', text):
    print('연도로 시작하는 문자열입니다.')
else:
    print('연도로 시작하지 않습니다')

text = '2026년 9월 21일'
if m := re.match(r'\d{4}', text):
    print(f'매칭된 연도: {m.group()}')
else:
    print('매칭 실패')
    
m = re.match(r'\d*', 'abc')
print(m)

print(bool(m))

m = re.fullmatch('[a-z]+', 'hel53lo')
print(m)

m = re.match('[a-z]+', 'hel53lo')
print(m)

m = re.fullmatch('[a-z]+', 'Hello')
print(m)

m = re.fullmatch('[a-zA-Z]+', 'Hello')
print(m)

print(re.fullmatch(r'\d+', '12345'))
print(re.fullmatch(r'\d+', '123 45'))
print(re.fullmatch(r'\d+', '123a'))
print(re.fullmatch(r'\d+', ''))

print(re.fullmatch(r'\d{5}', '31234'))
print(re.fullmatch(r'\d{5}', '3123'))
print(re.fullmatch(r'\d{5}', '312345'))

print(re.match(r'\d{5}', '312345'))

phone_pattern = r'01[016789]-\d{3,4}-\d{4}'

print(re.fullmatch(phone_pattern, '010-1234-5678'))
print(re.fullmatch(phone_pattern, '011-123-4567'))
print(re.fullmatch(phone_pattern, '010-12-5678'))
print(re.fullmatch(phone_pattern, '02-1234-5678'))
print(re.fullmatch(phone_pattern, '010-1234-56789'))

id_pattern = r'[a-z][a-z0-9_]{3,11}'

print(re.fullmatch(id_pattern, 'python3'))
print(re.fullmatch(id_pattern, 'user_name_01'))
print(re.fullmatch(id_pattern, '3python'))
print(re.fullmatch(id_pattern, 'abc'))
print(re.fullmatch(id_pattern, 'Python3'))
print(re.fullmatch(id_pattern, 'user_name_0123'))

print(re.match(r'[a-z]+$', 'hello\n'))
print(re.fullmatch(r'[a-z]+', 'hello\n'))
print(re.fullmatch(r'[a-z]+$', 'hello\n'))

print(re.match('a|ab', 'ab'))

print(re.fullmatch('a|ab', 'ab'))

num1 = "010-1234"
num2 = "0101234"
pattern = r'010-?\d{4}'
print(bool(re.match(pattern, num1)))
print(bool(re.match(pattern, num2)))

email = "abcd@domain.com"
if re.fullmatch(r'[a-z0-9]+@[a-z]+\.(com|net|org)', email):
    print("match.....")
else:
    print("nono!!!")
    
name_pattern = r'[가-힣]{2,4}'

print(re.fullmatch(name_pattern, '홍길동'))
print(re.fullmatch(name_pattern, '남궁민수'))
print(re.fullmatch(name_pattern, '김'))
print(re.fullmatch(name_pattern, '홍길동전설'))
print(re.fullmatch(name_pattern, '홍길동1'))

date_pattern = r'\d{4}-\d{2}-\d{2}'

print(re.fullmatch(date_pattern, '2026-09-21'))

print(re.fullmatch(date_pattern, '2026-9-21'))
print(re.fullmatch(date_pattern, '2026/09/21'))
print(re.fullmatch(date_pattern, '2026-09-21 '))

print(bool(re.fullmatch(date_pattern, '2026-09-21')))
print(bool(re.fullmatch(date_pattern, '2026/09/21')))

email_pattern = r'[\w.+-]+@[\w-]+(\.[\w-]+)+'

print(re.fullmatch(email_pattern, 'python@example.com'))
print(re.fullmatch(email_pattern, 'my.name+tag@mail.co.kr'))
print(re.fullmatch(email_pattern, 'python@example'))
print(re.fullmatch(email_pattern, '@example.com'))
print(re.fullmatch(email_pattern, 'python@example.com'))
print(re.fullmatch(email_pattern, 'my.-.name+.-tag@email.co.kr'))

def is_valid_phone(text: str) -> bool:
    return bool(re.fullmatch(r'01[016789]-\d{3,4}-\d{4}', text))

print(is_valid_phone('010-1234-5678'))
print(is_valid_phone('010-1234-567'))
print(is_valid_phone('전화번호'))

pattern = r'[a-z]+'
texts = ['hello', 'hello123', '123hello']

for text in texts:
    m1 = 'O' if re.match(pattern, text) else 'X'
    m2 = 'O' if re.fullmatch(pattern, text) else 'X'
    print(f'{text:10} match: {m1:3} fullmatch: {m2:3}')
    
PHONE_PATTERN = re.compile(r'01[016789]-\d{3,4}-\d{4}')
ID_PATTERN = re.compile(r'[a-z][a-z0-9_]{3,11}')
PYTHON_PATTERN = re.compile(r'python', re.IGNORECASE)

print(PHONE_PATTERN.fullmatch('010-1234-5678'))
print(PHONE_PATTERN.fullmatch('010-12-5678'))
print(ID_PATTERN.fullmatch('python3'))
print(PYTHON_PATTERN.match('Python is fun'))

numbers = [
    '010-1234-5678',
    '011-123-4567',
    '02-123-4567',
    '010-abcd-5678'
]
for num in numbers:
    result = '유효' if PHONE_PATTERN.fullmatch(num) else '형식 오류'
    print(f'{num} -> {result}')
    
print(re.match(r'\d{5}', '312345'))
print(re.fullmatch(r'\d{5}', '312345'))
print(re.match(r'\d+', '주문번호 12345'))

m = re.fullmatch(r'\d+', 'abc')
if m:
    print(m.group())

print(re.fullmatch(r'\d*', ''))
print(re.fullmatch(r'\d+', ''))

print(re.fullmatch(r'\d+', '٣٤٥'))
print(re.fullmatch(r'[0-9]+', '٣٤٥'))
print(re.fullmatch(r'\d+', '٣٤٥', re.ASCII))