"""
사람 클래스 (Person)
- 이름/주민등록번호
Person을 상속 받는 사원 클래스 만들기 (Employee)
- 이름/주민등록번호/회사명/연봉

==> 필요한 메서드는 적당히 만들어서 추가해보기
"""

class Person:
    def __init__(self, name, sn):
        self.set_name(name)
        self.set_sn(sn)
        
    def print_info(self):
        print(f"이름: {self.get_name()}")
        print(f"주민등록번호: {self.get_sn()}")
        
    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'name' must be string")
        self.name = name
        
    def get_name(self) -> str:
        return self.name

    def set_sn(self, sn: str):
        if not isinstance(sn, str):
            raise TypeError("'sn' must be string")
        self.sn = sn
        
    def get_sn(self) -> str:
        return self.sn

class Employee(Person):
    def __init__(self, name: str, sn: str, company: str, salary: int):
        super().__init__(name, sn)
        self.set_company(company)
        self.set_salary(salary)
        
    def print_info(self):
        super().print_info()
        print(f"회사명: {self.get_company()}")
        print(f"연봉: {self.get_salary()}원")
        
    def set_company(self, company: str):
        if not isinstance(company, str):
            raise TypeError("'company' must be string")
        self.company = company

    def get_company(self) -> str:
        return self.company
    
    def set_salary(self, salary: int):
        if not isinstance(salary, int):
            raise TypeError("'salary' must be integer")
        if salary < 0:
            raise ValueError("'salary' cannot be negative")
        self.salary = salary
        
    def get_salary(self) -> int:
        return self.salary

e = Employee("홍길동", "991212-1777777", "애플", 80000000)
e.print_info()