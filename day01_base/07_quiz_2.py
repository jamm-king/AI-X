# 변수 age가 65 이상이면 "경로우대", 19세 이상이면 "성인", 그 외에는 "미성년자"를 출력하는 if-elif-else문을 작성하세요.
age = int(input("나이 입력: "))
if age >= 65:
    print("경로우대")
elif age >= 19:
    print("성인")
else:
    print("미성년자")