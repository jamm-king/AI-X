# money = 1000
# print("현재 잔액 =>", money)
# while money > 0:
#     n = int(input("얼마짜리 살 거야? => "))
#     if n > money:
#         print("잔액이 부족해~")
#         print("남은 잔액 =>", money)
#         continue
#     money = money - n
#     print("남은 잔액 =>", money)
    
# 단을 입력 받아서 구구단을 출력해보세요 -> for문
# n = int(input("단 입력: "))
# for i in range(1, 10):
#     print(f"{n} * {i} = {n*i:>2}")

# while문 바꿔보기
n = int(input("단 입력: "))
i = 1
while i < 10:
    print(f"{n} * {i} = {n*i:>2}")
    i += 1