"""
4. 여러 개의 숫자 점수를 매개변수로 전달받아(개수 제한 없이) 최고점을 반환하는 함수를 만들고 각각 호출해 보세요.
"""

def max_score(*scores):
    return max(*scores)

scores = [100, 90, 95, 130, 50, 55]
print("scores:", *scores)
print("max score:", max_score(scores))