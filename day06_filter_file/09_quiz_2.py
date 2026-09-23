"""
2. flowers.txt파일의 꽃이름 모두를 읽어와 화면에 출력해 보세요
"""

with open("flowers.txt", "r", encoding="utf-8") as f:
    flowers = f.readlines()
    for flower in flowers:
        print(flower.strip())