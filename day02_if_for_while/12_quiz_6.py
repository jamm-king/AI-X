# 문제 6. 임의의 정수를 입력받아, 1부터 입력받은 수까지의 합을 구해서 출력하는 코드를 작성하세요. (for문 이용)

n = int(input("정수 입력: "))
tot = 0
for i in range(1, n + 1):
    tot += i
print(f"1부터 {n}까지의 총합: {tot}")