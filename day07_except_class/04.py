# try:
#     a = int(input("정수 입력: "))
#     b = int(input("나눌 정수 입력: "))
#     c = a / b
#     print(f"{a} / {b} = {c}")
# except ValueError as v:
#     print(f"숫자로 입력해주세요: [{type(v)}]", v)
# except Exception as e:
#     print(f"에러발생: [{type(e)}]", e)
# else:
#     print("예외가 발생하지 않고 잘 연산했어요!")
# finally:
#     print("예외가 나든 안 나든 상관 없이 무조건 수행돼요!")

def get_age(age):
    if age < 0:
        raise ValueError("나이는 0 미만일 수 없어요")
    return age - 1

try:
    age = get_age(10)
    print("만 나이:", age)
    age = get_age(-10)
    print("만 나이:", age)
    
except ValueError as v:
    print(v)