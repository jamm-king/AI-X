def get_price(name: str) -> int:
    prices = {
        "사과": 1000,
        "바나나": 1500,
        "체리": 3000
    }
    return prices.get(name, 0)

if __name__ == '__main__':
    
    # given
    name1 = "사과"
    name2 = "포도"

    # when
    result1 = get_price(name1)
    result2 = get_price(name2)

    # then
    assert result1 == 1000, f"사과 가격 오류: {result1}원 나옴"
    assert result2 == 0, f"없는 과일 가격 오류: {result2}원 나옴"

    print("테스트 통과")