"""
1. 꽃이름 5개을 입력받아 flowers.txt파일로 저장해 보세요
"""

with open("flowers.txt", "w", encoding="utf-8") as f:
    flowers_str = input("꽃 이름 입력: ")
    flowers = flowers_str.split(" ")
    for flower in flowers:
        f.write(flower + "\n")