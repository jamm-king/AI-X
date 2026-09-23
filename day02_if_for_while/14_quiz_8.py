# 문제 8. while문을 이용해 사용자가 "종료"라는 문자열을 입력할 때까지 계속 입력을 받아 출력하는 코드를 작성하세요.

while True:
    string = input("입력: ")
    if(string == "종료"):
        break