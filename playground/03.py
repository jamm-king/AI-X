class Person:
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
p = Person("홍길동", 30)
print(p._Person__name)