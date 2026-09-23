"""
1. 동물이름을 입력받아 리스트에 추가하고 모두 출력해보세요.
"""

animals = []
print("동물 입력:")
while True:
    animal = input()
    if animal == "":
        break
    animals.append(animal)
    
print("전체 동물:", *animals)