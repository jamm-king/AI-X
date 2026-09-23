"""
문제 1
사용자로부터 숫자를 입력받아(`input()`), 100을 그 숫자로 나눈 결과를 출력하는 코드를 작성해 보세요.
단, 사용자가 숫자가 아닌 값을 입력하거나 0을 입력해도 프로그램이 멈추지 않고 각각 적절한 안내 메시지를 출력하도록 예외처리 하세요.
"""
try:
    num = int(input("숫자 입력: "))
    print(f"100 / {num} = {100 / num:.2f}")
    
except ValueError:
    print("숫자를 입력해주세요.")
    
except ZeroDivisionError:
    print("0 으로 나눌 수 없습니다.")
    