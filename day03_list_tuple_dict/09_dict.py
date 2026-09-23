person = {
    "name": "홍길동",
    "age": 30,
    "phone": "010-111-1234"
}
print(person)
print(person["name"])
print(person.get("age"))
print(person.get("phone"))
print(person.get("city", "Seoul"))
person["email"] = "hello@gmail.com"
person["age"] = 10
print(person)

# 학생번호: key, 점수: value
stu_scores = {
    1: 100,
    2: 30,
    3: 80,
    4: 60,
    5: 90
}
# 학생번호를 입력받아 학생의 점수를 출력해보세요.
stu_num = int(input("학생번호 입력: "))
print(f"{stu_num}번 학생 점수: {stu_scores.get(stu_num, "없는 번호입니다.")}")

# 아이디와 비밀번호, 이메일에 대한 정보를 갖는 딕셔너리를 만들고 각 값들을 출력해보세요
d = {
    "id": "admin",
    "pw": "1234",
    "email": "admin@gmail.com"
}

for key in d.keys():
    print(f"{key}: {d.get(key)}")