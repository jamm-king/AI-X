# 문제 1. 리스트 nums = [5, 3, 8, 1, 9, 2]가 있을 때, 이 리스트에서 짝수만 골라 새로운 리스트 evens를 만드는 코드를 작성하세요. (반복문 사용)

nums = [5, 3, 8, 1, 9, 2]
print("전체:", *nums)
evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)

print("짝수:", *evens)