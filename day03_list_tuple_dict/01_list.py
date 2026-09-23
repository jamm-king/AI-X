names = ["조안나", "황희연", "김준용", "도창국", "김대성", "진정영"]
for name in names:
    print(f"{name}님")
print("-------------")
print(names[0])
names.append("김효진") # 리스트에 추가 -> 맨마지막에 추가
names.insert(1, "전희수") # 1번 위치에 추가
print("-------------")
print(names)
print("-------------")
names.remove("조안나")
print(names)
del_name = names.pop()
print(names)
print("삭제된 이름 ==>", del_name)
del names[0] # 인덱스 위치로 삭제(0번째 이름 삭제)
print(names)
names.remove(names[0])
print(names)