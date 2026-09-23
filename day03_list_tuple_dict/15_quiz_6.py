# 문제 6. set_a = {1, 2, 3, 4}와 set_b = {3, 4, 5, 6}이 있을 때, 두 집합의 합집합과 **차집합(a-b)**을 각각 구해서 출력하는 코드를 작성하세요.

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("set_a:", set_a, "\nset_b:", set_b)

print("합집합:", set_a | set_b)
print("차집합:", set_a - set_b)