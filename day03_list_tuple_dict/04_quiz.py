a = [10, 30, 90, 95, 40, 70, 22, 10, 50, 70]
print("점수:", *a)
# 학생 점수의 전체 총점 / 평균 구해서 출력해보세요
score_sum = 0
score_avg = 0

for score in a:
    score_sum += score
    
score_avg = score_sum / len(a)

print(f"총점: {score_sum}, 평균: {score_avg}")

# 학생 점수 중에서 가장 높은 점수 구하기
score_max = a[0]

for score in a:
    if score > score_max:
        score_max = score
        
print(f"최고점: {score_max}")