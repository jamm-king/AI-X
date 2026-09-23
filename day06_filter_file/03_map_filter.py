def get_pow(n):
    return n ** 2

a = get_pow(2)
print(2)
a = get_pow(4)
print(a)

get_pow = lambda n: n ** 2
b = get_pow(100)
print(b)
c = [1, 2, 3, 33, 44, 555]
d = list(map(get_pow, c))
print(d)

c = [44, 55, 66, 77, 88]
d = list(map(lambda n: n**2, c))
print(d)

e = list(filter(lambda n: n > 10, c))
print(e)

# 모든 아이디를 대문자로 변환해서 새로운 리스트에 저장되도록 해보세요
# map을 사용해서 해보세요
ids = ["hello", "blue", "happy"]
ids_upper = list(map(lambda s: s.upper(), ids))
print(ids_upper)

# 짝수만 걸러내기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 60점 이상인 학생만 걸러내기
scores = [55, 90, 60, 45, 88]
passed = list(filter(lambda x: x >= 60, scores))
print(passed)