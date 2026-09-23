"""
5.
nums = [3, 7, 1, 9, 4, 6]
리스트에 들어 있는 홀수들만 리스트로 만들어보세요(리스트 컴프리헨션 사용)
"""

nums = [3, 7, 1, 9, 4, 6]
print("전체 수:", *nums)

odds = [n for n in nums if n % 2 == 1]
print("홀수만:", *odds)