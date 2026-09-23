"""
[사원정보를 갖는 클래스 만들기]
생성자에서 사원번호/이름/연봉에 대한 정보를 매개변수로 전달받아 멤버변수에 저장한다.
사원번호/이름/(한달)급여/연봉을 출력하는 기능을 갖는 메서드를 만든다.
사원 클래스를 생성하고 정보를 출력해본다.
"""

class Employee:
    
    __slots__ = ["id", "name", "salary_annual"]
    
    def __init__(self, id: int, name: str, salary_annual: int):
        self.id = id
        self.name = name
        self.salary_annual = salary_annual
        
    def set_info(self, id: int, name: str, salary_annual: int):
        self.validate_info(id, name, salary_annual)
        self.id = id,
        self.name = name,
        self.salary_annual = salary_annual
        
    def print_info(self):
        print(f"[{self.id}] {self.name} - 급여: {self.salary_monthly}원, 연봉: {self.salary_annual}원")
        
    def validate_info(self, id: int, name: str, salary_annual: int):
        if not isinstance(id, int):
            raise TypeError("id must be integer")
        if not isinstance(name, str):
            raise TypeError("name must be string")
        if not isinstance(salary_annual, int):
            raise TypeError("salary_annual must be integer")
        if id < 1:
            raise ValueError("id must be positive")
        if salary_annual < 1:
            raise ValueError("salary_annual must be positive")
        
    @property
    def salary_monthly(self) -> int:
        return int(self.salary_annual / 12)
        
e = Employee(1, "홍길동", 40000000)
e.print_info()