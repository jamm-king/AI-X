"""
학생이름,국어,수학점수를 파일에 저장하고 파일에 저장된 데이터를 읽어와 총점,평균을 계산하고 화면에 출력하는 기능을 갖는 클래스를 만들고 사용하는
파이썬 코드를작성하시오
=> 클래스를 패키지를 만들어서 사용해 보세요
"""
from quiz05 import Student
from quiz05 import Repository

def test_case():
    students = [
        Student("홍길동", 90, 100),
        Student("김영희", 80, 100)
    ]
    
    Repository.save_all(students)
    loaded_students = Repository.load_all()
    for s in loaded_students:
        print(s)
    
    
if __name__ == "__main__":
    test_case()