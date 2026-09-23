# 문제 4. 임의의 정수를 입력받아 절대값을 구하는 코드를 작성해 보세요

n = int(input("정수 입력: "))
dist = n if n > 0 else -n
print(f"절대값: {dist}")