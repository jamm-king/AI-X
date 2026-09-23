"""
사각형
- x, y 좌표
- 사각형 그리기
"""

# class Rect:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def draw_rect(self):
#         print(f"{self.x}, {self.y} 위치에 사각형 그리기")
#     def paint_rect(self):
#         print(f"좌표 ==>", self.x, self.y)
#         print("사각형 칠하기")
        
# rect = Rect(1, 2)
# rect.draw_rect()
# rect.paint_rect()

# class Dog:
#     def __init__(self):
#         self.name = name
#         print("강아지가 태어났어요")

#     def bark(self):
#         print("멍멍멍 ~~~")

# dog1 = Dog()
# dog1.bark()
# dog2 = Dog()
# dog2.bark()

# class Book:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#     def bookinfo(self):
#         print(f"{self.title} - {self.price}")

# book1 = Book("헌터헌터", "30000원")
# book2 = Book("슬램덩크", "50000원")

# book1.bookinfo()
# book2.bookinfo()

# 학생번호, 국어, 수학 점수를 입력바당 학생 정보를 출력하고 총점을 계산해서 출력하기
class Student:
    def __init__(self, stu_no: str, score_kor: int, score_math: int):
        self.stu_no = stu_no
        self.score_kor = int(score_kor)
        self.score_math = int(score_math)
        self.score_total = score_kor + score_math
    def __str__(self):
        return f"[{self.stu_no}] 국어: {self.score_kor:>3}, 수학: {self.score_math:>3}, 총점: {self.score_total:>3}"

students = [
    Student(1, 80, 90),
    Student(2, 80, 80),
    Student(3, 100, 90),
    Student(4, 80, 100)
]
for student in students:
    print(student)
    