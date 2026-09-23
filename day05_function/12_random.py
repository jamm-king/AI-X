import random

print(random.random())

print(random.randint(1, 10))

fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

print(random.sample(range(1, 46), 6))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)