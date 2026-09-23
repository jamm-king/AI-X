"""
1. 정수를 매개변수로 전달받아 절대값을 구해서 리턴하는 함수를 만들고 사용해보세요
2. 정수를 매개변수로 전달받아 짝수인지 홀수인지 출력하는 함수를 만들고 사용해보세요
"""

def my_abs(n):
    return n if n > 0 else -n

nums = [1, -5, -6, 3, -4, 9]
for num in nums:
    print(f"|{num}| = {my_abs(num)}")
    
def even_or_odd(n):
    print("짝수") if n % 2 == 0 else print("홀수")

nums = [1, 2, 3, 4 , 5, 6, 7, 8]
for num in nums:
    print(f"{num} => ", end="")
    even_or_odd(num)