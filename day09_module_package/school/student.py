class Student:
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("'name' must be string")
        self._name = value
        
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'age' must be integer")
        if value < 0:
            raise ValueError("'age' cannot be negative")
        self._age = value
        
    def info(self):
        return f"이름: {self.name}, 나이: {self.age}"

# Student 객체를 생성하고 이름과 나이를 지정한 후 출력되는 코드를 작성해보세요

if __name__ == '__main__':

    # case 1: 일반 케이스
    
    # given
    name = "홍길동"
    age = 20
    
    # when
    student = Student(name, age)
    
    # then
    assert student.name == "홍길동", f"이름 저장 오류: {student.name}"
    assert student.age == 20, f"나이 저장 오류: {student.age}"
    assert student.info() == "이름: 홍길동, 나이: 20", f"info() 출력 오류: {student.info()}"
    
    # case 2: 이름에 잘못된 타입(정수)을 넣었을 때 TypeError 검증
    
    # given
    invalid_name = 12345
    
    # when & then
    try:
        Student(invalid_name, 20)
        assert False, "이름에 숫자를 넣었으나 TypeError가 발생하지 않았습니다."
    except TypeError as e:
        assert str(e) == "'name' must be string", f"엉뚱한 에러 메시지: {e}"
        
    # case 3: 나이에 잘못된 타입(문자열)을 넣었을 때 TypeError 검증
    
    # given
    invalid_age_type = "20"
    
    # when & then
    try:
        Student("홍길동", invalid_age_type)
        assert False, "나이에 문자열을 넣었으나 TypeError가 발생하지 않았습니다."
    except TypeError as e:
        assert str(e) == "'age' must be integer", f"엉뚱한 에러 메시지: {e}"
        
    # case 4: 나이에 음수를 넣었을 때 ValueError 검증
    
    # given
    invalid_age_value = -20
    
    # when & then
    try:
        Student("홍길동", invalid_age_value)
        assert False, f"나이에 음수를 넣었으나 ValueError가 발생하지 않았습니다."
    except ValueError as e:
        assert str(e) == "'age' cannot be negative", f"엉뚱한 에러 메시지: {e}"
        
    print("테스트 통과")