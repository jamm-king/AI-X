"""
3. 3명의 학생 이름/국어/수학 점수를 입력받아 score.txt파일에 저장하시오

score.txt
홍길동,100,40
이길동,10,50
삼길동,30,40
"""

with open("score.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        name = input("이름: ")
        kor = input("국어: ")
        eng = input("영어: ")
    
        f.write(f"{name},{kor},{eng}\n")