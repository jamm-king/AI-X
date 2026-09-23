# """
# < 파일 입출력 >
# - 단계
# 1. 파일을 열기
# 2. 원하는 작업 구현(읽기 / 쓰기)
# 3. 파일을 닫기
# """

# f = open("hello.txt", "w", encoding="utf-8")
# f.write("안녕하세요!\n")
# f.write("제 이름은 이재민입니다.\n")
# f.close()
f = open("아리랑.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
print(line1.strip())
print(line2.strip())
f.close()
print("---------------------------------------------")
f = open("아리랑.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()
print("파일을 모두 읽었어요~~~~")
print("---------------------------------------------")
f = open("아리랑.txt", "r", encoding="utf-8")
data = list(map(lambda line: line.strip(), f.readlines()))
print(data)
f.close()