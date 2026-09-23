"""
문제 5. Bank 클래스를 만드세요.
money(잔액)를 갖고, in_(amt)로 입금, out(amt)로 출금하되 잔액보다 많이 출금하려 하면 "부족"을 출력하도록 작성하세요.
"""

class Bank:
    
    def __init__(self, money: int):
        self.money = money

    @property
    def money(self) -> int:
        return self._money

    @money.setter   
    def money(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'money' must be integer")
        if value < 0:
            raise ValueError("'money' cannot be negative")
        self._money = value

    def in_(self, amt):
        if not isinstance(amt, int):
            raise TypeError("'amt' must be integer")
        if amt < 0:
            raise ValueError("'amt' cannot be negative")
        self.money += amt

    def out(self, amt):
        if not isinstance(amt, int):
            raise TypeError("'amt' must be integer")
        if amt < 0:
            raise ValueError("'amt' cannot be negative")
        if self.money < amt:
            raise ValueError("'amt' cannot be bigger than 'money'")
        self.money -= amt
        
class Interface:
    
    def __init__(self):
        self.bank = Bank(100000)
        self.amt = 0
        self.oper = None
        self.cont = '1'
        
    @property
    def amt(self) -> int:
        return self._amt
        
    @amt.setter
    def amt(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'amt' must be integer")
        if value < 0:
            raise ValueError("'amt' cannot be negative")
        self._amt = value

    @property
    def oper(self) -> str:
        return self._oper

    @oper.setter
    def oper(self, value: str):
        if value is None:
            self._oper = value
            return
        if not isinstance(value, str):
            raise TypeError("'oper' must be string")
        if value != '1' and value != '2':
            raise ValueError("'oper' must be '1' or '2'")
        self._oper = value
    
    @property
    def cont(self) -> str:
        return self._cont
    
    @cont.setter
    def cont(self, value: str):
        if not isinstance(value, str):
            raise TypeError("'cont' must be string")
        if value != '1' and value != '2':
            raise ValueError("'cont' must be '1' or '2'")
        self._cont = value
    
    def console_input_amt(self):
        self.amt = int(input("금액: "))
    
    def console_input_operation(self):
        self.oper = input("서비스를 선택해주세요.\n1) 입금  2) 출금 ")
        
    def console_input_continue(self):
            self.cont = input("계속 이용하시겠습니까?\n1) 예  2) 아니요 ")
        
    def execute(self):
        if self.oper == '1':
            self.bank.in_(self.amt)
            print(f"{self.amt}원 입금했습니다.\n현재 잔액: {self.bank.money}")
        else:
            try:
                self.bank.out(self.amt)
                print(f"{self.amt}원 출금했습니다.\n현재 잔액: {self.bank.money}")
            except ValueError:
                print(f"잔액 부족.\n현재 잔액: {self.bank.money}")
                
    def print_bank(self):
        print(f"{self.bank.money}")
        
    def print_line(self):
        print("------------------------")
    
def usecase():
    interface = Interface()
    while interface.cont == '1':
        try:
            interface.console_input_operation()
            interface.console_input_amt()
        except Exception:
            print("잘못된 입력입니다.")
        else:
            interface.execute()
        finally:
            while True:
                try:
                    interface.console_input_continue()
                    interface.print_line()
                    break
                except Exception:
                    print("잘못된 입력입니다.")
        
if __name__ == '__main__':
    usecase()