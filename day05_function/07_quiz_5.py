"""
5. 이름과 여러 개의 취미를 매개변수로 전달받아 "철수님의 취미는 축구, 게임 입니다." 형식으로 출력하는 함수를 만들고 사용해 보세요.
(취미 개수는 가변적으로 받을 것)
"""

def info(name, *hobbies):
    hobby_str = ""
    for hobby in hobbies:
        hobby_str += f"{hobby}, "
    hobby_str = hobby_str[:-2]
    print(f"{name}님의 취미는 {hobby_str} 입니다.")
    
info("길동", "축구", "농구", "게임")