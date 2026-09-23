"""
1. 학생이름과 연락처를 입력받아 연락처.txt 파일로 저장해 보세요

## 저장형태
홍길동,010-111-1234
이길동,010-222-3333
삼영희,010-333-4444
"""

with open("연락처.txt", "w", encoding="utf-8") as f:
    while True:
        name = input("이름: ")
        if name == "": break
        phone = input("연락처: ")
        if phone == "": break
        
        f.write(f"{name},{phone}\n")
        