def total(items: list) -> int:
    return sum(items)

if __name__ == '__main__':
    
    # given
    items = [1000, 1500, 2000]
    
    # when
    tot = total(items)
    
    # then
    assert tot == 4500, f"총 가격 오류: {items} -> {tot}"
    
    print("테스트 통과")