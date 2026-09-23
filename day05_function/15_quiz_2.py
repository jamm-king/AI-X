"""
2. 두 개의 숫자를 매개변수로 전달받아, 나눈 나머지를 반환하는 함수를 만들고 사용해 보세요.(람다함수 사용)
"""
li = [
    (5, 2),
    (10, 15),
    (100, 3),
    (123445, 1234)
]
print("(a, b):", *li)

remainder = lambda a, b: a % b

# print("a를 b로 나눈 나머지:", *list(map(remainder, li)))
print("a를 b로 나눈 나머지:", *[remainder(a, b) for a, b in li])