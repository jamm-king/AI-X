# 정수를 3개를 전달받아 세 수의 합을 구해서 반환하는 함수를 만들고 사용해보세요.

def my_sum(a, b, c):
    return a + b + c

li = [
    (1, 2, 3),
    (10, 20, 30),
    (0, 5, 10)
]

for a, b, c in li:
    print(f"{a} + {b} + {c} = {my_sum(a, b, c)}")

def get_tot(s):
    tot = 0
    for n in s:
        tot += n
    return tot
    
# 점수들의 평균을 구해서 리턴하는 함수를 만들고 사용해보세요

scores = [100, 30, 40, 50, 10]
scores_num = get_tot(scores)
print("점수총합", scores_num)

def my_avg(li):
    tot = 0
    for n in li:
        tot += n
    return tot / len(li)

print("scores:", *scores)
print("avg:", my_avg(scores))

def get_all(s):
    tot = get_tot(s)
    avg = tot/len(s)
    return tot, avg
a, b = get_all(scores)
print(a, b)

s = sum(scores)
ma = max(scores)
mi = min(scores)
le = len(scores)
print(s, ma, mi, le)

def greet(name, greeting="안녕하세요!"):
    print(f"{greeting} {name}님!")
greet("홍길동")
greet("홍길동", "안녕!")

def introduce(name, age, city):
    print(f"이름: {name}, 나이: {age}, 사는 곳: {city}")
introduce(age=25, city="서울", name="홍길동")

def choice(color="흰색", size=90):
    print("색상 =>", color)
    print("사이즈 =>", size)
choice("빨강", 100)
choice(size=100)
choice(color="빨강")

# 언패킹
a, b, c = (1, 2, 3)
a, b, c = [1, 2, 3]
print(a, b, c)
a, b, *c = [1, 2, 3, 4, 5, 6, 7]
print(a, b, c)
a, *b, c = [1, 2, 3, 4, 5, 6, 7]
print(a, b, c)
*a, b, c = [1, 2, 3, 4, 5, 6, 7]
print(a, b, c)
a = ["장미꽃", "개나리"]
b = ["무궁화", "진달래"]
print(a)
print(b)
b.append(a)
print(b)
b.remove(a)
print(b)
b.extend(a)
print(b)

def print_all(*a):
    print(a)
    print(type(a))

print_all(1, 2, 3)
print_all(1, 2, 3, 4, 5)

# 아래처럼 함수가 호출 가능하도록 my_sum 함수 만들기
# my_sum은 모든 인수값들을 더해서 반환한다
# s1 = my_sum(1, 2, 3)
# s2 = my_sum(1, 2, 3, 4)

def my_sum(*nums):
    tot = 0
    for num in nums:
        tot += num
    return tot
nums = [1, 2, 3, 4, 5]
print("nums:", *nums)
print("my sum:", my_sum(*nums))

def print_info(**info):
    print(info)
    for key, value in info.items():
        print(f"{key}=>{value}")

print_info(name="홍길동", age=20, city="서울")