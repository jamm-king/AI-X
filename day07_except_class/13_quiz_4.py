"""
4. 사각형의 가로,세로길이를 입력받아 넓이를 구해서 출력하는 기능을 클래스로 만들고 사용해 보세요.
"""

class Rect:
    
    def __init__(self, width: int = 0, height: int = 0):
        self.set_info(width, height)
        
    def __str__(self):
        return f"width: {self.width}, height: {self.height}, area: {self.area}"
    
    def set_info(self, width: int = 0, height: int = 0):
        self.validate_info(width, height)
        self.width = width
        self.height = height
        
    def validate_info(self, width: int = 0, height: int = 0):
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width and height must be integer")
        if width < 0 or height < 0:
            raise ValueError("width and height cannot be negative")
        
    @property
    def area(self) -> int:
        return self.width * self.height
    
class Interface:
    def __init__(self, figure):
        self.figure = figure
        
    def get_console_input(self):
        input_data = dict()
        print("### INPUT ###")
        for key in self.figure.__dict__:
            input_data[key] = int(input(f"{key}: "))
        self.figure.set_info(**input_data)
        
    def print_console(self):
        print("### OUTPUT ###")
        print(self.figure.__str__())
        
def usecase_rect():
    interface = Interface(Rect())
    interface.get_console_input()
    interface.print_console()
        
if __name__ == '__main__':
    try:
        usecase_rect()
    except Exception as e:
        print(e)