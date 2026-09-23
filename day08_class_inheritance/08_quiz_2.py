"""
문제 2. Counter 클래스를 만드세요. 클래스 변수 num으로 인스턴스 개수를 세고, @classmethod로 num을 반환하는 get_num()을 작성하세요.
"""

class Counter:
    
    num = 0
    
    def __init__(self):
        self.__class__.num += 1
        
    @classmethod
    def get_num(cls) -> int:
        return cls.num
    
counters = []
for i in range(10):
    counters.append(Counter())
    print(Counter.get_num())