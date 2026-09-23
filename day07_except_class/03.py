# while True:
#     try:
#         a = int(input("정수 입력(-1을 입력하면 종료됩니다.): "))
#         if a == -1: break
#         b = int(input("나눌 정수 입력: "))
#         c = a / b
#         print(f"{a} / {b} = {c}")
        
#     except ZeroDivisionError as z:
#         print("0으로 나눌 수 는 없어요. 다시 입력해주세요")
#         print("에러메시지 ==>", z)
        
# try:
#     a = int(input("정수 입력: "))
#     b = int(input("나눌 정수 입력: "))
#     c = a / b
#     print(f"{a} / {b} = {c}")
# except ZeroDivisionError as z:
#     print("0 으로 나눌 수 없습니다.")
#     print("에러메시지 ==>", z)
# except ValueError as v:
#     print("입력값은 숫자로 입력해주세요.")
#     print("에러메시지 ==>", v)

# 파일이 존재하지 않을 때 [파일이 존재하지 않습니다.] 라고 출력되도록
# 예외 처리를 해보세요.
try:
    with open("아리랑2.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError as file_not_found_error:
    print("파일이 존재하지 않습니다.", file_not_found_error)