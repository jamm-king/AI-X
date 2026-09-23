"""
다음은 학생 5명의 성적 정보가 저장된 리스트이다.
students = [
    {"name": "홍길동", "kor": 80, "eng": 75, "math": 90},
    {"name": "이길동", "kor": 70, "eng": 85, "math": 88},
    {"name": "박길동", "kor": 90, "eng": 92, "math": 95},
    {"name": "최길동", "kor": 60, "eng": 65, "math": 70},
    {"name": "정길동", "kor": 88, "eng": 79, "math": 84}
]

 - for문을 사용하여 각 학생의 총점과 평균을 출력하시오.
[출력결과]
홍길동 - 총점: 245, 평균: 81.67
이길동 - 총점: 243, 평균: 81.00
박길동 - 총점: 277, 평균: 92.33
최길동 - 총점: 195, 평균: 65.00
정길동 - 총점: 251, 평균: 83.67


- 전체 학생 평균 점수 구하기

- 평균이 80점 이상인 학생 이름 출력하기
80점 이상 학생: 홍길동, 이길동, 박길동, 정길동

- 최고 평균 점수를 받은 학생 출력하기
최고 평균 학생: 박길동 (92.33)
"""

students = [
    {"name": "홍길동", "kor": 80, "eng": 75, "math": 90},
    {"name": "이길동", "kor": 70, "eng": 85, "math": 88},
    {"name": "박길동", "kor": 90, "eng": 92, "math": 95},
    {"name": "최길동", "kor": 60, "eng": 65, "math": 70},
    {"name": "정길동", "kor": 88, "eng": 79, "math": 84}
]

scores = dict()
high_score_students = list()
max_score_student = None
max_score_avg = 0

for student in students:
    name = student.get("name")
    score_kor = student.get("kor")
    score_eng = student.get("eng")
    score_math = student.get("math")
    
    score_total = score_kor + score_eng + score_math
    score_avg = score_total / 3
    
    scores.update({
        name: {
            "총점": score_total,
            "평균": score_avg
        }
    })
    
    if score_avg >= 80:
        high_score_students.append(name)
    
    if score_avg > max_score_avg:
        max_score_avg = score_avg
        max_score_student = (name, score_avg)
    
for name in scores.keys():
    score = scores.get(name)
    score_total = score.get("총점")
    score_avg = score.get("평균")
    print(f"{name} - 총점: {score_total}, 평균: {score_avg:.2f}")
    
print("80점 이상 학생:", *high_score_students)

print(f"최고 평균 학생: {max_score_student[0]} ({max_score_student[1]:.2f})")