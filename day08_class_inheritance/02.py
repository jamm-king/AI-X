class Circle:
    
    def __init__(self, r = 10):
        self.r = r
        
    def set_r(self, r: float):
        self.r = r
        
    def get_r(self) -> float:
        return self.r
    
    def get_area(self) -> float:
        return self.r ** 2 * 3.1415
    
    def print_info(self) -> None:
        print("반지름 =>", self.r)
        print("원의 넓이 =>", f"{self.get_area():.2f}")
        
# 객체를 생성하고 원의 넓이가 구해져서 출력되는 코드를 완성해보세요.
c = Circle()
c.print_info()
c.set_r(20)
c.print_info()