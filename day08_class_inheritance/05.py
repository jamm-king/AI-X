class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"이름:{self.name}")
        print(f"나이:{self.age}")

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    def study(self):
        print(f"{self.name}이 공부를 합니다.")
    def introduce(self):
        super().introduce()
        print(f"전공: {self.major}")
    
s = Student("홍길동", 20, "컴퓨터공학")
s.introduce()
s.study()