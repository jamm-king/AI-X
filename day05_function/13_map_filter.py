a = [10, 20, 30, 40, 50]
def twice(n):
    return n * 2
result = list(map(twice, a))
print(result)

a = [-10, 20, -30]
def my_abs(n):
    return n if n > 0 else -n
b = list(map(my_abs, a))
c = list(map(abs, a))
print(b)
print(c)

print("----------------------")
a = [10, 20, 30, 40, 50]
result = list(map(lambda n: n*2, a))
print(result)

print("----------------------")

a = [-10, 20, -30]
def my_abs(n):
    return n if n > 0 else -n

# b = list(map(my_abs, a))
b = list(map(lambda n: n if n > 0 else -n, a))
print(b)

print("----------------------")

# map 함수를 사용해서 대문자로 변환된 리스트를 만들어보세요.
li = ["python", "java", "c"]
li_upper = list(map(lambda a: a.upper(), li))
print(li_upper)