"""
문제1)
클래스 이름: Student
요구사항:
이름(name), 점수(score) 변수를 가진다.
생성자로 이름과 점수를 초기화한다.
print_grade() 메소드에서 점수가 90 이상이면 "A", 80 이상이면 "B", 그 외는 "C"를 출력한다.
"""

class Student:
    
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("'name' must be string")
        self._name = value
        
    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'score' must be integer")
        self._score = value
        
    def print_grade(self):
        if self.score >= 90:
            print("A")
        elif self.score >= 80:
            print("B")
        else:
            print("C")
            
students = [
    Student("홍길동", 95),
    Student("김영희", 85),
    Student("박철수", 65)
]

for student in students:
    print(f"이름: {student.name}, 점수: {student.score}")