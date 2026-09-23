a = [10, 20, 30, 40, 50]
b = []
# a의 각 요소에 2배 곱한 값이 b리스트에 저장하기
for n in a:
    b.append(n*2)
print(b)
# 리스트 컴프리헨션
a = [10, 20, 30, 40, 50]
b = [n*2 for n in a]
print(b)
s1 = ["홍길동", "이길동", "삼길동", "오길동"]
s2 = set([s[0] for s in s1])
print(s2)

c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [n if n % 2 == 0 else -n for n in c]
print(d)

e = [1, 2, 3]
# 리스트 컴프리헨션을 사용해서 e의 요소값들의 제곱값을
# 새로운 리스트에 담아서 출력해보세요. [1, 4, 9]
ee = [n**2 for n in e]
print(ee)

f = [100, 30, 40, 60, 10, 80]
# 리스트 컴프리헨션을 사용해서 점수가 80 이상인
# 요소들만 새로운 리스트에 담아서 출력해보세요. [100, 80]
ff = [n for n in f if n >= 80]
print(ff)

s1 = [
    {
        '번호': 1,
        '점수': 80
    },
    {
        '번호': 2,
        '점수': 90
    },
    {
        '번호': 3,
        '점수': 50
    },
    {
        '번호': 4,
        '점수': 60
    }
]
# 점수만 리스트에 저장
s2 = [s['점수'] for s in s1]
print(s2)
# 컴프리핸션을 사용해서 점수가 70점 이상인 데이터만 리스트로 저장
s3 = [s['점수'] for s in s1 if s['점수'] >= 70]
print(s3)


# 1. 리스트 컴프리헨션이란 ?

# 기존 방식
squares = []
for i in range(1, 6):
    squares.append(i ** 2)

print(squares)

# 리스트 컴프리헨션
squares = [i ** 2 for i in range(1, 6)]

print(squares)

# 2. 기본 문법
numbers = [1, 2, 3, 4, 5]

doubled = [n * 2 for n in numbers]
print(doubled)

words = ["apple", "banana", "cherry"]

upper_words = [w.upper() for w in words]
print(upper_words)

lengths = [len(w) for w in words]
print(lengths)

# 3. 조건문 포함하기 - if로 걸러내기
# 기존 방식: 짝수만 골라내기
numbers = [1, 2, 3, 4, 5, 6, 7 , 8 , 9, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
        
print(evens)

# 리스트 컴프리헨션
numbers = [1, 2, 3, 4, 5, 6, 7 , 8 , 9, 10]
evens = [n for n in numbers if n% 2 == 0]

print(evens)

# 4. 조건에 따라 다른 값 넣기 - if / else
scores = [55, 90, 60, 45, 88]

result = ["합격" if s >= 60 else "불합격" for s in scores]
print(result)

# 5. 중첩 반복문 사용하기

# 기존 방식: 구구단 2 ~ 3단 결과를 하나의 리스트로
result = []
for i in range(2, 4):
    for j in range(1, 4):
        result.append(i * j)

print(result)

# 리스트 컴프리헨션
colors = ["빨강", "파랑"]
sizes = ["S", "M"]

combos = [f"{c}-{s}" for c in colors for s in sizes]
print(combos)

# 6. 딕셔너리 컴프리헨션 / 세트 컴프리헨션

# 딕셔너리 컴프리헨션
names = ["철수", "영희", "민수"]

name_lenghts = {name: len(name) for name in names}
print(name_lenghts)

numbers = [1, 2, 3, 4, 5]

squares_dict = {n: n**2 for n in numbers}
print(squares_dict)

# 세트 컴프리헨션
words = ["apple", "banana", "apple", "cherry", "banana"]

unique_lengths = {len(w) for w in words}
print(unique_lengths)

# 7. 언제 컴프리헨션을 쓰면 좋을까 ?
result = []
for n in range(1, 20):
    if n % 3 == 0 and n % 5 == 0:
        result.append("fizzbuzz")
    elif n % 3 == 0:
        result.append("fizz")
    elif n % 5 == 0:
        result.append("buzz")
    else:
        result.append(str(n))
        
print(result)

# 8. 종합 예제
scores = [55, 90, 78, 45, 88, 92, 60, 33, 100, 71]

# 1) 60점 이상인 점수만 추출
passed = [s for s in scores if s >= 60]
print("합격 점수:", passed)

# 2) 모든 점수에 5점씩 가산점 부여 (최대 100점)
adjusted = [min(s + 5, 100) for s in scores]
print("가산점 적용:", adjusted)

# 3) 점수별 합격/불합격 라벨링
labels = ["합격" if s >= 60 else "불합격" for s in scores]
print("합격 여부:", labels)

# 4) 점수 -> 합격 여부 딕셔너리 매핑
score_result = {s: "합격" if s >= 60 else "불합격" for s in scores}
print("점수별 결과:", score_result)

# 실습 문제
# 문제 1. range(1, 11)을 이용해 1~10의 세제곱(n ** 3) 리스트를 리스트 컴프리헨션으로 만드세요.
li = [n**3 for n in range(1, 11)]
print(li)

# 문제 2. 문자열 리스트 ["hi", "hello", "hey", "good morning"]에서 길이가 4 이하인 단어만 리스트 컴프리헨션으로 추출하세요.
li = ["hi", "hello", "hey", "good morning"]
li = [s for s in li if len(s) <= 4]
print(li)

# 문제 3. range(1, 21)의 숫자 중 3의 배수는 "fizz", 아니면 그 숫자 그대로를 담은 리스트를 if/else 리스트 컴프리헨션으로 만드세요.
li = ["fizz" if n % 3 == 0 else n for n in range(1, 21)]
print(li)

# 문제 4. 리스트 [1, -2, 3, -4, 5, -6]에서 절댓값이 3 이상인 수만 골라, 그 절댓값으로 이루어진 새 리스트를 리스트 컴프리헨션으로 만드세요.
li = [1, -2, 3, -4, 5, -6]
li = [abs(n) for n in li if abs(n) >= 3]
print(li)

# 문제 5. 단어 리스트 ["apple", "banana", "cherry"]를 이용해, 단어를 키로 첫 글자를 값으로 하는 딕셔너리를 딕셔너리 컴프리헨션으로 만드세요.
li = ["apple", "banana", "cherry"]
li = [{w: w[0]} for w in li]
print(li)