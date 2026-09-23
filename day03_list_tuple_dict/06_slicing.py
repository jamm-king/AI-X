scores = [55, 66, 33, 44, 10, 30, 40, 50]
print(scores)
a = scores[0:3]
print(a)
print(scores[1:5])
print(scores[1:])
print(scores[:4])
print(scores[:])
print(scores[-1])
print(scores[-2])
print(scores[-3:-1])
print(scores[-3:])

# 리스트에 저장된 데이터가 타입이 달라도 가능
stu_info = ["홍길동", "11111111", 10, 20, 30]
print(stu_info)
stu_info = ["홍길동", "1234", [100, 30, 40]]
print(stu_info)
print("-------------------------------------")
print(stu_info[0])
print(stu_info[2][0])
print(stu_info[2][1])
s = "Hello world"
print(s[1])
print(s[1:5])
print(s[1:])
print(s[-1])
print(s[-2:])
# Hello 글자만 추출해서 출력하기
print(s[:5])
# world 글자만 추출해서 출력하기
print(s[6:])