"""
4. scores = {
    "철수": 90,
    "영희": 80
}
딕셔너리의 모든 key값(이름)을 출력하세요.
전체 점수의 총점과 평균을 구해보세요
"""

scores = {
    "철수": 90,
    "영희": 80
}

score_sum = 0
score_avg = 0
for name, score in scores.items():
    score_sum += score
    print(name, end=" ")
print()
score_avg = score_sum / len(scores)
print(f"평균: {score_avg}")