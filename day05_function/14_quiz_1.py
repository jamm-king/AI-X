"""
1. 숫자를 매개변수로 전달받아, 절댓값을 구해서 반환하는 함수를 만들고 사용해 보세요.(람다함수 사용)
"""

li = [1, -2, -3, 4, 5, -6]
print("전체 수:", *li)

my_abs = lambda n: n if n > 0 else -n

print("절대값:", *list(map(my_abs, li)))