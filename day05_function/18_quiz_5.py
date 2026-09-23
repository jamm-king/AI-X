"""
5. 숫자 리스트를 매개변수로 전달받아, map을 사용해서 각 숫자를 제곱한 리스트를 반환하는 함수를 만들고 사용해 보세요.
"""

nums = [1, 2, 3, 4, 5]
print("nums:", *nums)

def pow_all(nums):
    return list(map(lambda num: num ** 2, nums))

print("제곱:", *pow_all(nums))