# 사용자 정의 함수
def my_tot(a, b):
    c = a + b
    return c

a, b = 10, 20
c = my_tot(a, b)
print(f"{a} + {b} = {c}")

# 반지름을 전달 받아 원의 넓이를 구하는 함수 (원의 넓이: 반지름 * 반지름 * 3.14)
def circle_area(r):
    area = r * r * 3.14
    return area

a = circle_area(10.5)
print(f"원의 넓이 = {a}")

# 가로, 세로 길이를 매개변수로 전달받아 사각형의 넓이를 구해서 반환하는 함수를 만들고 사용해보세요.
def rect_area(width, height):
    return width * height

cases = [(20, 10), (15, 30), (5, 5), (12, 8)]
for width, height in cases:
    area = rect_area(width, height)
    print(f"가로: {width}, 세로: {height}, 넓이: {area}")

# 나이를 매개변수로 전달 받아서 나이가 19세 이상이면 "성인" 아니면 "미성년자"라고 반환하는 함수를 만들고 사용해보세요.
def check_adult(age):
    return "성인" if age >= 19 else "미성년자"

ages = [19, 22, 45, 13, 8, 34, 27]
for age in ages:
    print(f"{age}세는 {check_adult(age)}입니다.")
    
def my_math(a, b):
    c = a + b
    d = a - b
    return c, d
n1, n2 = my_math(10, 20)
print("--------------------------")
print(n1, n2)