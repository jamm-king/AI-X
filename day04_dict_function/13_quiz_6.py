"""
6. 임의의 정수를 두개 매개변수로 전달받아 두 수중 큰값을 구해서 반환하는 함수를 만들고 사용해보세요.
"""

li = [
    (1, 2),
    (10, 10),
    (-9, 9),
    (144, 144.5)
]

def my_max(a, b):
    return a if a > b else b

for a, b in li:
    print(f"{a}, {b} 중 큰 값은 {my_max(a, b)}입니다.")