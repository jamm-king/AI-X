"""
[상속]
class 부모 클래스:
    # 부모 클래스의 속성과 메서드 정의

class 자식 클래스:
    # 부모의 속성을 상속받고, 필요한 경우 메서드 오버라이딩 가능
"""

class Animal:
    def __init__(self, name):
        print("parent")
        self.name = name
    def speak(self):
        print(f"{self.name}이(가) 소리를 냅니다.")
    def print_info(self):
        print(f"name: {self.name}")

class Dog(Animal):
    def __init__(self, name, age):
        print("child")
        super().__init__(name)
        self.age = age
    def run(self):
        print(f"{self.name}이(가) 달려가요~~~")
    def print_info(self):
        super().print_info()
        print(f"age: {self.age}")

dog = Dog("바둑이", 10)
dog.print_info()
dog.speak()
dog.run()