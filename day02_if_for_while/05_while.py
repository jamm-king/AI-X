count = 0
while count < 5:
    print(count)
    count += 1
    
# 1부터 100까지 수를 출력하고 합을 구해서 출력하기 -> while문
i = 1
tot = 0
while i <= 100:
    print(i, end=" ")
    tot += i
    i += 1
    
print()
print(f"1부터 100까지의 합: { tot }")

# while문을 사용해서 1부터 100까지 수 중 짝수만 출력해보세요
i = 2
while i <= 100:
    print(i, end=" ")
    i += 2
print()
    
# while문을 사용해서 1부터 100까지 수 중 짝수합/홀수합 구해서 출력해보기
i = 1
even_sum = 0
odd_sum = 0
while i <= 100:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i += 1
    
print(f"짝수 합: { even_sum }, 홀수 합: { odd_sum }")

while True:
    input_pwd = input("비밀번호 입력: ")
    if input_pwd == "1234":
        print("비밀번호가 맞습니다.")
        break
    else:
        print("비밀번호가 맞지 않습니다..")