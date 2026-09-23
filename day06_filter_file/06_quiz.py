# movies = ["맨인블랙", "캐리비안의 해적", "인터스텔라"]

# with open("movies.txt", "w", encoding="utf-8") as f:
#     for movie in movies:
#         f.write(movie + "\n")
        
# with open("movies.txt", "r", encoding="utf-8") as f:
#     data = list(map(lambda s: s.strip(), f.readlines()))
#     for idx, movie in enumerate(data):
#         print(f"{idx + 1}. {movie}")

# 3명의 학생이름과 전화번호를 입력받아서 파일로 저장하기
with open("연락처.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        name = input("학생이름 입력: ")
        phone = input("전화번호 입력: ")
        f.write(f"{name},{phone}\n")
print("파일로 저장완료!!!!!")
print("파일에 저장된 정보 읽어오기............")
with open("연락처.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())