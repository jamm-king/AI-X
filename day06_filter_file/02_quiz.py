"""
반지름(실수) 매개변수로 전달받아 원의 넓이를 반환하는 함수를 만들고 사용해 보세요. 함수의 반환타입은 실수임
"""

def area_circle(radius: float) -> float:
    return radius ** 2 * 3.1415

r = 5
print(f"반지름 길이가 {r}인 원의 넓이는 {area_circle(r):.2f}입니다.")

"""
5명의 학생점수를 리스트로 전달받아 전체 총점과 평균을 출력하는 함수를 만들고 사용해 보세요. 함수에서 반환값은 없음
"""

def print_total_and_average(
    scores:list[int]
) -> None:
    tot = sum(scores)
    avg = tot / len(scores)
    print("scores:", scores)
    print("tot:", tot, "avg:", avg)

scores = [80, 70, 75, 95, 100]
print_total_and_average(scores)

"""
가로길이, 세로길이를 매개변수로 전달받아 사각형 넓이를 구해 반환하는 함수를 만들고 사용해 보세요.
매개변수의 타입힌트는 int또는 None이 올 수 있으며 None이 전달되면 None이 리턴되도록 코드를 작성하세요..
"""

def area_rect(
    width: int | None = None,
    height: int | None = None
) -> int | None:
    if width == None or height == None:
        return None
    
    return width * height

width, height = 10, 20
print("width:", width, "height:", height, "area:", area_rect(width, height))
width, height = None, 30
print("width:", width, "height:", height, "area:", area_rect(width, height))