fruits = ("포도", "사과", "바나나", "딸기")
print(fruits)
for fruit in fruits:
    print(fruit)
# fruits[0] = "수박" # 에러 -> 튜플은 값변경 불가

pays = (200, 400, 350, 1000)
# 튜플에 저장된 급여를 2배 인상해서 리스트에 저장하고 출력해보세요.
# 400, 800, 700, 2000
pays_list = [pay * 2 for pay in pays]
print(*pays_list)