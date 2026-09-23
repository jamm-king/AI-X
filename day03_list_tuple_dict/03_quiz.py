"""
1. 10명의 학생 점수을 입력 받아 전체 점수를 모두 출력해보세요.
2. 점수가 80점 이상인 점수만 출력되게 해보세요
"""
scores = []
high_scores = []

scores_str = input("점수 입력: ")
scores = [int(score) for score in scores_str.split(" ")]
for score in scores:
    if score >= 80:
        high_scores.append(score)
        
print(f"전체 점수({len(scores)}명):", *scores)
print(f"80점 이상 점수({len(high_scores)}명):", *high_scores)
