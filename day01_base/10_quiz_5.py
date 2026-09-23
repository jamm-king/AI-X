# 리스트 cart = ["우유", "빵", "계란"]에 "계란"이 포함되어 있으면 "장바구니에 계란이 있습니다", 그렇지 않으면 "장바구니에 계란이 없습니다"를 출력하는 if문을 작성하세요.
cart = ["우유", "빵", "계란"]
product = input("상품 입력: ")
if product in cart:
    print(f"장바구니에 { product }이(가) 있습니다")
else:
    print(f"장바구니에 { product }이(가) 없습니다")