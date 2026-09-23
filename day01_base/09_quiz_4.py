# 변수 sotck(재고 수량)이 0이면 "품절", 10 미만이면 "재고 부족", 그 외에는 "재고 충분"을 출력하는 if-elif-else문을 작성하세요.
stock = int(input("재고 수량 입력: "))
if stock == 0:
    print("품절")
elif stock < 10:
    print("재고 부족")
else:
    print("재고 충분")