add = lambda a, b : a + b
minus = lambda a, b : a - b
def calc(oper, a, b):
    return oper(a, b)

a, b = 1, 2

print(f"{a} + {b} = {calc(add, a, b)}")
print(f"{a} - {b} = {calc(minus, a, b)}")

# def twice(n):
#     return n * 2

twice = lambda n : n * 2
n = twice(10)
print(n)

# def get_max(a, b):
#     return a if a > b else b

get_max = lambda a, b : a if a > b else b
m = get_max(1, 2)
print(m)

# 정수를 매개변수로 전달받아 절대값을 구하는 함수를 람다함수로 만들고 사용해보세요
my_abs = lambda n : n if n > 0 else -n
li = [1, 3, -2, -6, 10]
for n in li:
    print(f"|{n}| = {my_abs(n)}")

# 파라미터로 반지름을 전달받아 원의 넓이를 람다함수를 사용해서 만들고 사용해보세요
area_circle = lambda r : (r ** 2) * 3.1415
li = [1, 2, 3, 4 , 5]
for n in li:
    print(f"반지름 길이가 {n}인 원의 넓이는 {area_circle(n):.2f}입니다.")