a = [10, 20, 30, 40]
print(a[0])
print(a[0:3])
print(a[:3])
print(a[3:])
print(a[-1])
print(a[:])
print(a[::-1])

b = {
    1: 100,
    2: 30,
    3: 40,
    4: 55,
    5: 10
}
print(type(b))
# 2번 학생의 점수 출력
print(b[2])
print(b.get(2))
print(b)

scores = {
    "1": 100,
    "2": 40,
    "3": 50,
    "4": 90
}
for s in scores:
    print(s)

for s in scores.keys():
    print(s, type(s))
print("------------------------")
for num, score in scores.items():
    print(f"번호: {num}, 점수: {score}")

students = {
    "홍길동": "010-111-1234",
    "이길동": "010-222-0000",
    "삼길동": "010-333-4444",
}
# 전체 학생의 이름을 출력해보세요(전체 key값 출력해보기)
for student in students:
    print(student, end=" ")
print()

# 전체 학생이름과 연락처를 모두 출력해보세요.
for name, phone in students.items():
    print(name, ":", phone)
    
# 학생이름을 입력받아서 해당 연락처를 출력하기
find_name = input("학생이름 입력: ")
if find_name in students:
    phone = students[find_name]
    print(f"{find_name}학생 연락처 => {phone}")
else:
    print("학생이름이 존재하지 않아요.")
    
# 전체 총점을 구하기
scores = {
    "1": 100,
    "2": 40,
    "3": 50,
    "4": 90
}
for _, score in scores.items():
    print(score, end=" ")
print()

score_sum = 0
for _, score in scores.items():
    score_sum += score
print("총점:", score_sum)

stu = {
    "name": "홍길동",
    "score": 80
}
# 점수가 70 이상이면 합격 아니면 불합격 출력
if stu.get("score") >= 70:
    print("합격")
else:
    print("불합격")