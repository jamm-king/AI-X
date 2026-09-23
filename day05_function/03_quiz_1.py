"""
1. 국어, 영어 점수를 매개변수로 전달받아 평균을 구해서 반환하는 함수를 만들고 사용해 보세요.
"""

def avg(kor, eng):
    return (kor + eng) / 2

kor = 90
eng = 85

print(f"국어: {kor}, 영어: {eng}, 평균: {avg(kor, eng)}")