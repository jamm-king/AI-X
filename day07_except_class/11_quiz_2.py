"""
2. 연락처.txt파일에서 학생정보를 읽어와서 
학생이름으로 해당 전화번호를 출력해 보세요. (파일이 존재하지 않을경우 예외처리를 하세요)
예) 학생이름입력:홍길동
조회된 이름:홍길동
연락처:010-111-1234
"""
students = dict()
try:
    with open("연락처.txt", "r", encoding="utf-8") as f:
        for line in f:
            name, phone = line.strip().split(",")
            students.update({name: phone})
except FileNotFoundError:
    print("'연락처.txt' 파일이 존재하지 않습니다.")
    
stu_name = input("학생이름입력:")
try:
    stu_phone = students[stu_name]
    print(f"조회된 이름:{stu_name}")
    print(f"연락처:{stu_phone}")
except KeyError:
    print("학생을 찾을 수 없습니다.")