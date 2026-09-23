"""
도서 정보를 생성자의 매개변수로 전달받아 값을 지정하고
도서 정보를 출력하는 멤버 메서드를 갖는 클래스를 만들고 사용해보세요

도서 정보
- 도서 이름
- 저자
- 가격
"""

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
    def __str__(self):
        return f"[{self.name:^10}] 저자: {self.author:>10}, 가격: {self.price:>7}"
    def print_info(self):
        print(self.__str__())
        
books = [
    Book("노인과 바다", "헤밍웨이", "15000원"),
    Book("헌터X헌터", "토가시 요시히로", "6000원")
]

for book in books:
    book.print_info()