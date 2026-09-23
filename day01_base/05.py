# 임의의 정수를 입력받아 짝수/홀수 판별하기
# num = int(input("임의의 정수를 입력하세요=>"))
# a = num % 2
# if a == 0:
#     print(f"{ num }은 짝수입니다.")
# else:
#     print(f"{ num }은 홀수입니다.")

# 국어, 면접 점수를 입력 받아서 국어 >= 80, 면접 >= 90 => 합격
# kor = int(input("국어 점수: "))
# interview = int(input("면접 점수: "))
# if kor >= 80 or interview >= 90:
#     print("당신은 합격입니다!!!")
# else:
#     print("당신은 불합격입니다!!!")

# score = int(input("당신의 점수를 입력해보세요: "))
# if score >= 90:
#     print("A등급")
# elif score >= 80:
#     print("B등급")
# elif score >= 70:
#     print("C등급")
# else:
#     print("D등급")

# 임의의 정수를 입력 받아서 양수인지 음수인지 0인지 출력해 보세요
# n = int(input("정수 입력: "))
# if n > 0:
#     print("양수입니다.")
# elif n < 0:
#     print("음수입니다.")
# else:
#     print("0입니다.")
    
# 아이디와 비밀번호를 입력 받아 맞으면 로그인 틀리면
# 아이디 또는 비밀번호를 확인하세요
user_id = input("아이디 입력: ")
user_pwd = input("비밀번호 입력: ")
if user_id == "admin" and user_pwd == "1234":
    print("관리자로 로그인 성공!!!")
else:
    print("아이디 또는 비밀번호가 맞지 않습니다.")