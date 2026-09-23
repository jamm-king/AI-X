"""
문제 1. Book 클래스를 만드세요. title, price를 인스턴스 변수로 갖고, 정보를 출력하는 show() 메서드를 작성하세요.
"""

class Book:
    
    def __init__(self, title: str, price: int):
        self.set_title(title)
        self.set_price(price)
        
    def show(self):
        print(f"{self.get_title()} : {self.get_price()}원")
        
    def set_title(self, title: str):
        if not isinstance(title, str):
            raise TypeError("title must be str")
        
        self.title = title
        
    def get_title(self) -> str:
        return self.title
    
    def set_price(self, price: int):
        if not isinstance(price, int):
            raise TypeError("price must be int")
        if price < 0:
            raise ValueError("price cannot be negative")
        
        self.price = price
        
    def get_price(self) -> int:
        return self.price

if __name__ == '__main__':
    book = Book("노인과 바다", 13000)
    book.show()