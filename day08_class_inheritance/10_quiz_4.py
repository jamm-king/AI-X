"""
문제 4. Student(이름, 국어, 영어, 수학)를 상속받는 Top 클래스를 만드세요.
avg()를 오버라이딩해서, 평균이 90 이상이면 "우등생", 아니면 "보통"을 출력하는 check() 메서드를 추가하세요.
"""

class Student:
    
    def __init__(self, name: str, kor: int, eng: int, math: int):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        
    def avg(self):
        return (self.kor + self.eng + self.math) / 3

class Top(Student):
    
    def __init__(self, name: str, kor: int, eng: int, math: int):
        super().__init__(name, kor, eng, math)
    
    def check(self):
        avg = self.avg()
        if avg >= 90:
            print("우등생")
        else:
            print("보통")
            
t1 = Top("홍길동", 90, 100, 100)
t1.check()
t2 = Top("이길동", 80, 70, 70)
t2.check()