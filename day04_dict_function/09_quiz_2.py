"""
2. 회원이름을 튜플에 저장하고 전체 데이터를 출력해보세요.
"""

users_list = []
print("회원 입력:")
while True:
    user = input()
    if user == "":
        break
    users_list.append(user)
users_tuple = tuple(users_list)
users_tuple = users_tuple.__add__(("홍길동", "사길동"))

print("전체 회원:", *users_tuple)