students = [
    {
        "이름": "홍길동",
        "과목명": "수학",
        "점수": 100
    },
    {
        "이름": "김영희",
        "과목명": "과학",
        "점수": 90
    },
    {
        "이름": "이순이",
        "과목명": "영어",
        "점수": 60
    }
]
for stu in students:
    print(stu)
print("-----------------------------")
for stu in students:
    print(stu["이름"])
print("-----------------------------")
# 점수가 90점 이상인 학생의 이름을 출력해보세요
for student in students:
    if student.get("점수") >= 90:
        print(student.get("이름"), end=" ")
print()
print("-----------------------------")
students = {
    "홍길동": {
        "국어": 90,
        "수학": 85
    },
    "김철수": {
        "국어": 80,
        "수학": 95
    }
}
print(students.get("홍길동").get("국어"))
print(students.get("김철수").get("국어"))

# 전체 데이터도 출력해보세요
for name, scores in students.items():
    print(f"[{name}]", end=" ")
    row = "("
    for subject, score in scores.items():
        row += f"{subject}: {score}, "
    row = row[:-2] + ")"
    print(row)
