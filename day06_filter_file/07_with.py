# with open("memo.txt", "w", encoding="utf-8") as f:
#     f.write("오늘의 할일\n")
#     f.write("1. 파이썬 공부하기\n")
#     f.write("2. 저녁 운동하기\n")
# print("파일로 저장 완료!!!")

# with open("memo.txt", "r", encoding="utf-8") as f:
#     data = f.read()
#     print(data)

with open("memo.txt", "r", encoding="utf-8") as f:
    data = f.readline()
    print(data)
    data = f.readline()
    print(data)