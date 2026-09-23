# sort
numbers = [5, 2, 8, 1, 9]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

# other methods
numbers = [1, 3, 5, 3, 7, 3, 9]

print(numbers.count(3))
print(numbers.index(5))
print(len(numbers))

numbers.extend([11, 13])
print(numbers)

numbers.clear()
print(numbers)

# ex1)
cart = ["우유", "계란"]

cart.append("빵")

print(cart)

# ex2)
scores = [90, 85, 100, 70, 95]

total = sum(scores)
average = total / len(scores)

print("총점:", total)
print("평균:", average)

# ex3)
days = ["월", "화", "수", "목", "금"]

for day in days:
    print(day, "요일")

# ex4)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_half = numbers[:5]
second_half = numbers[5:]

print(first_half)
print(second_half)