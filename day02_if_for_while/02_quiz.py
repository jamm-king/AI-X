# a = """안녕하세요!
# 제 이름은 이재민입니다."""
# print(a)

# name = "이재민"
# b = f"""
# 반갑습니다.
# 제 이름은 { name }입니다.
# """
# print(b)

# a = "aaa"
# b = "aaa"
# print(a == b)
# print(a is b)

"""
Q1)
1부터 100까지 출력하기(한 줄에 숫자는 10개씩 출력하기)
1  2  3  4  5  6  7  8  9  10
11 12 13 ...               20
..
91 ...                     100

Q2)
1부터 100까지 수 중에서 3의 배수를 출력하고 3의 배수 합도 출력해보세요.

Q3)
리스트에 학생 이름 5명을 저장하고 모든 학생 이름을 출력해보세요.
"""

# Q1
for i in range(0, 10):
    for j in range(0, 10):
        num = i * 10 + j + 1
        print(f"{num:>4}", end=" ")
    print()
    
# Q2
sum = 0
for i in range(0, 100):
    num = i + 1
    if(num % 3 == 0):
        sum += num
        print(num, end=" ")
print(f"\n3의 배수 합: { sum }")

# Q3
input_names = input("학생 이름 입력(공백 구분): ")
names = input_names.split(" ")
print(*names)