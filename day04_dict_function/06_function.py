def get_area(r):
    area = r * r * 3.14
    print(f"원의 넓이: {area}")
get_area(10)

def rect_area(x, y):
    return x*y
a = rect_area(100, 200)
b = rect_area(400, 100)
if a > b:
    print("a 사각형이 넓어요")
else:
    print("b 사각형이 넓어요")
    
def greet(name=""):
    print(f"{name}님 반갑습니다!!!")
    
greet("길동이")
greet("순이")
greet()

def draw_rect(w=100, h=100):
    print(f"가로길이: {w}, 세로길이: {h}인 사각형을 그려요")

draw_rect(100, 200)
draw_rect(400,200)
draw_rect()