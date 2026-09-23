"""
가로길이, 세로길이를 사용자로부터 입력받아 사각형의 넓이를 구해 출력하는 코드를 작성해 보세요.
단, 입력받은 가로 또는 세로길이가 0 이하이면 raise를 이용해 직접 예외를 발생시키고,
그 예외를 except로 잡아서 "길이는 0보다 커야 합니다"라는 메시지를 출력하도록 하세요.
"""

try:
    width = int(input("가로: "))
    if width <= 0: raise ValueError("width length should be bigger than 0")
    height = int(input("세로: "))
    if height <= 0: raise ValueError("height length should be bigger than 0")
    
    area = width * height
    print(f"넓이: {area}")
    
except ValueError as v:
    print(f"[{type(v)}]", v)