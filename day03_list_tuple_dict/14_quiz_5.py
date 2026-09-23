# 문제 5. list_a = [1, 2, 2, 3, 4, 4, 5]에서 중복을 제거한 리스트를 셋을 이용해 만들고 출력하는 코드를 작성하세요.

list_a = [1, 2, 2, 3, 4, 4, 5]
print("list_a:", list_a)

list_b = list(set(list_a))
print("list_b:", list_b)