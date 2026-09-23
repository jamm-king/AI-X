"""
삼항연산자
[참일 때의 값] if [조건식] else [거짓일 때의 값]
"""

age = 20
result = "성인" if age >= 18 else "미성년자"
print(result)

"""
if ~ else 사용해서 두 수 중 큰 값 구해서 출력
"""
a = 10
b = 20
if a > b:
    print(a)
else:
    print(b)
    
# 삼항 연산자로 바꿔보세요
max = a if a > b else b
print(max)

"""
삼항 연산자를 사용해서 a가 짝수인지 홀수인지 출력
"""
a = 20
print("짝수") if a % 2 == 0 else print("홀수")