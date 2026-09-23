fruits = ["바나나", "포도", "수박"]
for num, f in enumerate(fruits):
    print(f"{num:0>2}: {f:>4}")
    

"""
구구단 전체 출력해보기
"""    
for i in range(1, 10):
    print("|", end=" ")
    for j in range(2, 10):
        print(f"{j} x {i} = {i*j:>2}", end=" | ")
    print()
    
print("-----------------------------")
    
for i in range(0, 5):
    for j in range(0, i + 1):
        print("*", end="")
    print()
    
print("-----------------------------")
    
"""
for문 사용해서 아래처럼 출력되도록 해보세요
*****
*****
*****
*****
*****
"""
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()