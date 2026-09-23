# 매개변수로 두 정수를 전달받아 두 정수 합을 구해서 반환하는 함수를 만들고 함수를 사용해서 두 수의 합을 구해서 출력해보세요

def my_sum(a, b):
    return a + b

a, b = 5, 2
print(f"{a} + {b} = {my_sum(a, b)}")

def add(a: int, b: int) -> int:
    return a + b

result = add(10, 20)    
print(f"두 수의 합 = {result}")

def add_str(a: str, b: str) -> str:
 return a + ", " + b

d = add_str("바나나", "포도")
print(d)

def print_insa(name: str) -> None:
    print(f"{name}님 반갑습니다!!!")

print_insa("길동이")

def func1(items: list[int]) -> None:
    for i, n in enumerate(items):
        print(f"{i}:{n}")

a = [10, 20, 30]
func1(a)
func1([40, 50, 60, 70, 10])

def func4(info: list[dict[str, str | int]]) -> None:
    print(info)

stu = [
    {
        "학생번호": 1,
        "이름": "홍길동"
    },
    {
        "학생번호": 2,
        "이름": "김영희"
    }
]
func4(stu)

def func8(name: str | None = None) -> None:
    print("name:", name)

func8("길동이")
func8()