# 변수 id가 "admin"이고, 변수 pw가 "1234"일 때만 "로그인 성공"을 출력하고, 그 외에는 "로그인 실패"를 출력하는 if문을 작성하세요.(and 연산자 사용)
id = input("아이디 입력: ")
pw = input("비밀번호 입력: ")
if id == "admin" and pw == "1234":
    print("로그인 성공")
else:
    print("로그인 실패")