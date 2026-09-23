"""
4. score.txt파일 전체 데이터를 읽어와 총점을 계산해서 전체 정보를 화면에 출력하세요
= 성적표 =
홍길동,100,40,140
이길동,10,50,60
삼길동,30,40,70
"""

with open("score.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, kor, eng = line.strip().split(",")
        tot = int(kor) + int(eng)
        
        print(f"{name},{kor},{eng},{tot}")