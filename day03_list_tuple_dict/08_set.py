# q1)
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)

# q2)
numbers = {1, 2, 3}
numbers.discard(100)
print(numbers)

# q3)
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

result = a & b
print(result)

# q4)
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)

# q5)
l = [1, 1, 2, 2, 3, 3, 4]
l = list(set(l))
print(l)

# add, update
fruits = {"사과", "바나나"}
fruits.add("포도")
print(fruits)
fruits.update(["딸기", "수박"])
print(fruits)

#remove, discard, clear
numbers = {1, 2, 3, 4, 5}

numbers.remove(3)
print(numbers)

numbers.discard(10)
print(numbers)

numbers.clear()
print(numbers)

# set operation
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
print(a | b)
print(a - b)
