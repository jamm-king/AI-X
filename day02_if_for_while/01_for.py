# names = ["홍길동", "이길동", "삼길동"]
# for name in names:
#     print(name)
    
# print("출력완료!!!")

# for i in range(1, 10):
#     print(i, end = " ")
    
# print()
# print("출력 끝!!!")


# 1부터 100까지 수를 출력하고 합을 구해서 출력하기
# tot = 0
# for i in range(0, 100):
#     num = i + 1
#     print(num, end=" ")
#     tot += num
    
# print()
# print(f"1부터 100까지의 합: { tot }")


# a가 짝수인지 홀수인지 판별하는 if문 작성해보세요
# a = 100
# if a % 2 == 0:
#     print(f"{ a }은(는) 짝수")
# else:
#     print(f"{ a }은(는) 홀수")

# # 1부터 100까지 수 중에서 짝수만 출력
# for i in range(0, 100):
#     num = i + 1
#     if num % 2 == 0:
#         print(num, end=" ")
        
# print()


# 1부터 100까지 수 중에서 홀수를 출력하고 홀수 합을 구해서 출력해보세요
# sum = 0
# for i in range(0, 100):
#     num = i + 1
#     if num % 2 == 1:
#         sum += num
#         print(num, end=" ")
        
# print(f"\n홀수 합은 { sum }")

# 아이디/비밀번호 입력 받아 모두 맞으면 관리자로 로그인 성공!
# 아이디나 비밀번호가 틀리면 맞지 않습니다. 출력
# for i in range(3):
#     id = input("아이디 입력: ")
#     pw = input("비밀번호 입력: ")
#     if id == "admin" and pw == "1234":
#         print("관리자로 로그인 성공!!!")
#         break
#     else:
#         print("아이디 또는 비밀번호를 확인하세요!!!")

# for i in range(1, 101, 2): # 1부터 100까지 2씩 증가 -> 홀수
#     print(i, end=" ")
    
word = "Hello"
for c in word:
    print(c, end=" ")