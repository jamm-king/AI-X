# 문제 2. 리스트 fruits = ['apple', 'banana', 'cherry']에 'orange'를 맨 앞에 추가하고, 최종 리스트를 출력하는 코드를 작성하세요.

fruits = ['apple', 'banana', 'cherry']
print("추가 전:", *fruits)

fruits.insert(0, 'orange')
print("추가 후:", *fruits)
