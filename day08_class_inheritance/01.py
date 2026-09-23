# 사각형의 가로, 세로 길이를 생성자 매개변수로 전달받아 넓이를 구해서 출력하는 클래스를 만들고 사용해보기

class Rect:
    
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    
    def print_area(self):
        print(self.area)
        
    @property
    def area(self):
        return self.width * self.height
        
if __name__ == '__main__':
    rect = Rect(20, 10)
    rect.print_area()
    Rect.print_area(rect)
    print(rect.area)