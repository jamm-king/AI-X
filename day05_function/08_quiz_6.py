"""
6. 학생의 이름, 국어점수, 영어점수, 수학점수를 매개변수로 전달받아 총점과 평균을 함께 반환(반환값 2개)하는 함수를 만들고,
반환받은 총점과 평균을 각각 변수에 담아 출력해 보세요.
"""

def get_sum_and_avg(name, score_kor, score_eng, score_math):
    score_sum = score_kor + score_eng + score_math
    score_avg = score_sum / 3
    return score_sum, score_avg

score_sum, score_avg = get_sum_and_avg("길동", 80, 90, 90)
print(f"총점: {score_sum}, 평균: {score_avg:.2f}")