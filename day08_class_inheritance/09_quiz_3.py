"""
문제 3. Person(부모)과 Teacher(자식) 클래스를 만드세요.
Person은 name을 갖고, Teacher는 name, subj(과목)를 받아 super()로 부모 생성자를 호출한 뒤, 소개하는 show()를 작성하세요.
"""

class Person:
    
    def __init__(self, name: str):
        self.name = name
        
class Teacher(Person):
    
    def __init__(self, name: str, subj: str):
        super().__init__(name)
        self.subj = subj
        
    def show(self):
        print(f"{self.name} ({self.subj})")
        
t = Teacher("홍길동", "국어")
t.show()