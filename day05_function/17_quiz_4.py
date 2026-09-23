"""
4. 숫자 리스트를 매개변수로 전달받아, 리스트의 모든 값이 짝수인지 확인해서 True/False로 반환하는 함수를 만들고 사용해 보세요. (all 사용)
"""

evens = [2, 4, 6, 8, 10]
mixed = [1, 2, 3, 4, 5]
print("evens:", *evens)
print("mixed:", *mixed)

def is_all_even(nums):
    return all(num % 2 == 0 for num in nums)

print("evens가 모두 짝수인가 ? =>", is_all_even(evens))
print("mixed가 모두 짝수인가 ? =>", is_all_even(mixed))