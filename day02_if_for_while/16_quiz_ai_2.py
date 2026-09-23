"""
퀴즈 2: 데이터 필터링 및 통계 구하기 (for + if)
학생들의 시험 점수 리스트가 주어졌을 때, 조건에 맞는 점수만 처리하는 프로그램을 만드세요.
초기 데이터: scores = [85, 42, 92, 58, 77, 61, 30, 99, 88]
요구사항:for문을 사용하여 scores 리스트의 점수를 하나씩 확인합니다.
60점 이상인 점수(합격점)만 따로 골라내어 합격자들의 총점과 평균 점수를 구하세요.
반복문이 끝난 후 "합격자 수: OO명, 총점: OO점, 평균 점수: OO.OO점" 형태로 출력하세요 (평균은 소수점 둘째 자리까지 출력).
"""

scores = [85, 42, 92, 58, 77, 61, 30, 99, 88]
pass_sum = 0
pass_cnt = 0
pass_avg = 0
for score in scores:
    if score >= 60:
        pass_sum += score
        pass_cnt += 1
pass_avg = float(pass_sum) / pass_cnt

print(f"합격자 수: {pass_cnt}명, 총점: {pass_sum}, 평균 점수: {pass_avg:.2f}점")