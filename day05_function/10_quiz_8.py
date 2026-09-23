"""
8. 숫자 리스트를 매개변수로 전달받아, 리스트 안의 짝수만 모아서 새로운 리스트로 반환하는 함수를 만들고 사용해 보세요.
"""

def extract_evens(nums):
    evens = list()
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens
    
nums = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
evens = extract_evens(nums)
print("전체 수:", *nums)
print("짝수:", *evens)