"""
 퀴즈 1: 은행 ATM 잔액 관리 및 출금 시스템 (while + if)
 사용자가 원하는 금액을 출금하는 간단한 ATM 시뮬레이터를 만드세요.
 초기 조건: 현재 계좌 잔액은 50,000원입니다.
 요구사항:while문을 사용하여 사용자가 0을 입력할 때까지 반복해서 출금 금액을 입력받습니다.
 출금할 금액이 현재 잔액보다 크다면 "잔액이 부족합니다."를 출력하고 출금하지 않습니다.
 출금할 금액이 잔액 이하이고 0보다 크다면, 잔액에서 해당 금액을 차감하고 "OO원이 출금되었습니다. 남은 잔액: OO원"을 출력합니다.
 사용자가 0을 입력하면 "서비스를 종료합니다. 최종 잔액은 OO원입니다."를 출력하고 반복문을 빠져나갑니다 (break 사용).
"""

money = 50000
withdrawal = 0
while True:
    withdrawal = int(input("출금 금액: "))
    if withdrawal > money:
        print("잔액이 부족합니다.")
    elif withdrawal > 0:
        money -= withdrawal
        print(f"{withdrawal}원이 출금되었습니다. 남은 잔액: {money}원")
    elif withdrawal == 0:
        print(f"서비스를 종료합니다. 최종 잔액은 {money}원입니다.")
        break