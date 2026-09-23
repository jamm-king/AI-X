"""
퀴즈 3: 369 게임 시뮬레이터 (for + if 응용)
1부터 30까지 숫자를 출력하되, 369 게임의 규칙을 따르는 코드를 작성하세요.
요구사항:for문과 range()를 사용하여 1부터 30까지 반복합니다.
숫자에 3, 6, 9가 포함되어 있다면 숫자 대신 짝수 기호인 "짝!"을 출력합니다.
3, 6, 9가 없다면 숫자 그대로를 출력합니다.
힌트: 숫자를 문자열(str)로 변환한 뒤, '3' in 문자열 같은 방식을 활용해 보세요.
"""

exceptions = ['3', '6', '9']
for i in range(1, 31):
    i_str = str(i)
    is_exception = False
    for e in exceptions:
        if e in i_str:
            print("짝!", end=" ")
            is_exception = True
            break
    if is_exception:
        continue
    print(i, end=" ")