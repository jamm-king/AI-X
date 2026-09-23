"""
1. 과일이름(str): key, 가격(int): value
형태로 저장하는 딕셔너리를 만들고 정보를 3개 저장해보세요.
2. 전체 과일이름과 가격을 출력해보세요.
3. 전체 과일 가격의 평균을 구해보세요.
"""

fruits = {
    "포도": 1000,
    "딸기": 2000,
    "바나나": 3000
}

cost_sum = 0
cost_avg = 0
for name, cost in fruits.items():
    cost_sum += cost
    print(f"{name}: {cost}원")
cost_avg = cost_sum / len(fruits)
print(f"평균: {cost_avg}원")