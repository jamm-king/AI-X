"""
6. 문자열 리스트를 매개변수로 전달받아, map을 사용해서 각 문자열의 길이를 담은 리스트를 반환하는 함수를 만들고 사용해 보세요.
"""

strings = ["Hello, world!", "Bye bye", "Goodbye"]
print("strings:", strings)

def length_string(strings):
    return list(map(len, strings))

print("lengths:", *length_string(strings))