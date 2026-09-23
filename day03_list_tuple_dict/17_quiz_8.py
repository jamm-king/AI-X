# 학생번호를 입력받아 해당 학생의 이름을 출력해 보세요.

d = {
    1: {
        "학생번호": 1,
        "이름": "홍길동",
        "과목": "국어",
        "점수": 30
    },
    2: {
        "학생번호": 2,
        "이름": "이길동",
        "과목": "수학",
        "점수": 80
    },
    3: {
            "학생번호": 3,
            "이름": "삼길동",
            "과목": "수학",
            "점수": 70
        }
}

for key in d.keys():
    stu = d.get(key)
    print(f"[{key}]", end="  ")
    row = ""
    for k in stu.keys():
        row += f"{k}: {stu.get(k)}, "
    row = row[:-2]
    print(row)

stu_num = int(input("학생번호 입력: "))
stu_name = d.get(stu_num).get("이름")
print(f"이름: {stu_name}")