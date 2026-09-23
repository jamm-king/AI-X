"""
1. 학생 성적 분석기
문제: 여러 학생의 이름과 국어, 영어, 수학 점수가 튜플로 묶여 리스트에 저장되어 있습니다.
이 데이터를 입력받아 각 학생의 평균 점수를 계산하고,
평균 점수가 높은 순으로 정렬된 결과를 반환하는 사용자 정의 함수 analyze_grades(student_data)를 작성하세요.
입력 예시:
students = [
    ("김철수", 85, 90, 78),
    ("이영희", 92, 88, 95),
    ("박민수", 70, 80, 85)
]
요구사항:
1. 각 학생의 평균 점수는 소수점 둘째 자리까지 반올림합니다.
2. 반환되는 결과는 [(이름, 평균점수), (이름, 평균점수), ...] 형태의 리스트여야 합니다.
3. 평균 점수를 기준으로 내림차순(높은 순) 정렬해야 합니다.
"""

students = [
    ("김철수", 85, 90, 78),
    ("이영희", 92, 88, 95),
    ("박민수", 70, 80, 85)
]

def analyze_grades(student_data):
    analyzed_data = list()
    for name, *scores in student_data:
        total = 0
        for score in scores:
            total += score
        avg = total / len(scores)
        
        for i, analyzed in enumerate(analyzed_data):
            if avg > analyzed[1]:
                pass