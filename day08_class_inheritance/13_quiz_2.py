"""
문제2)
Product 라는 이름의 클래스를 만들고  상품명과 가격을 생성자에서 멤버변수로 초기화 한다.
Product를 상속받는 Book클래스를 만들고 도서저자에 대한 정보가 추가된다.
-> 클래스 기능을 적당히 만들고 사용해 보세요
"""

class Product:

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("'name' must be string")
        self._name = value
        
    @property
    def price(self) -> int:
        return self._price
    
    @price.setter
    def price(self, value: int):
        if not isinstance(value, int):
            raise TypeError("'price' must be integer")
        if value < 0:
            raise ValueError("'price' cannot be negative")
        self._price = value
        
class Book(Product):
    
    def __init__(self, name: str, price: int, author: str):
        super().__init__(name, price)
        self.author = author
        
    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str):
        if not isinstance(value, str):
            raise TypeError("'author' must be string")
        self._author = value
        
    def print_info(self):
        print(f"이름: {self.name}")
        print(f"가격: {self.price}원")
        print(f"저자: {self.author}")
        
book = Book("노인과 바다", 13000, "헤밍웨이")
book.print_info()