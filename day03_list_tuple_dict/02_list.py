# items = []
# for i in range(3):
#     item = input("상품명을 입력하세요: ")
#     items.append(item)
# print(f"입력한 상품들: ", end="")
# print(*items)

scores = [30, 40, 20, 10, 90]
score_sum = 0
score_avg = 0
print("점수: ", end="")
for score in scores:
    score_sum += score
    print(score, end=" ")
print()
score_avg = float(score_sum) / len(scores)
print(f"총합: {score_sum}, 평균: {score_avg}")
