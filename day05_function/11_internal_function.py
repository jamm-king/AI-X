# .upper()
text = "abc"
print(text.upper())

# .lower()
text = "ABC"
print(text.lower())

# .strip()
text = "  ab  "
print(text.strip())

# .replace(a, b)
text = "ab"
print(text.replace("a", "c"))

# .split(기준)
text = "a, b"
print(text.split(","))

# "".join(리스트)
words = ["a", "b"]
print(",".join(words))

# .find(문자)
text = "abc"
print(text.find("b"))
print(text.find('z'))

# .count(숫자)
text = "aaa"
print(text.count("a"))

# .startswith(문자)
text = "abc"
print(text.startswith("a"))

# .endswith(문자)
text = "abc"
print(text.endswith("c"))

# len(문자열)
text = "abc"
print(len(text))

scores = [80, 90, 70, 60]
a = [score >= 90 for score in scores]
print(a)

flags1 = [True, False, False]
flags2 = [True, True, True]

print(any(flags1))

print(all(flags1))
print(all(flags2))

print("---------------------")

scores = [80, 90, 70, 60]

print(any(score >= 90 for score in scores))

print(all(score >= 60 for score in scores))
print(all(score >= 70 for score in scores))

print("---------------------")

nums1 = [0, 0, 3, 0]
nums2 = [1, 2, 3, 4]
nums3 = [1, 0, 3, 4]

print(any(nums1))

print(all(nums2))
print(all(nums3))

print("---------------------")

sentences = ["오늘 날씨가 좋다", "내일은 비가 온다", "모레는 맑음"]

print(any("비" in s for s in sentences))
print(all("날씨" in s for s in sentences))

print("---------------------")

students = [
    {
        "name": "철수",
        "score": 85
    },
    {
        "name": "영희",
        "score": 92
    },
    {
        "name": "민수",
        "score": 55
    }
]

has_excellent = any(s["score"] >= 90 for s in students)
print("90점 이상 학생 존재:", has_excellent)

all_passed = all(s["score"] >= 60 for s in students)
print("전원 합격 여부:", all_passed)

print("---------------------")


empty_list = []

print(any(empty_list))
print(all(empty_list))

print("---------------------")

username = "admin"
password = "1234"
email = ""
inputs = [username, password, email]

if not all(inputs):
    print("모든 항목을 입력해주세요.")
    
print("---------------------")

class Item:
    def __init__(self, name, left):
        self.name = name
        self.left = left
        self.is_soldout = True if self.left == 0 else False
    
piano = Item("피아노", 2)
guitar = Item("기타", 0)
flute = Item("플룻", 5)
cart_items = [piano, guitar, flute]

if any(item.is_soldout for item in cart_items):
    print("품절 상품이 포함되어 있습니다.")
    
print("---------------------")

numbers = [1, 2, 3, 4, 5, 6]

if all(x > 0 for x in numbers):
    print("모두 양수입니다.")
    
print("---------------------")

x, y, z = 1, 2, 3

if all(v > 0 for v in [x, y, z]):
    print("모두 양수입니다.")
    
print("---------------------")

numbers = [1, 2, 3, 4, 5]

# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)
squared = map(lambda x: x ** 2, numbers)
for s in squared:
    print(s)
for s in squared:
    print(s)

str_numbers = ["1", "2", "3"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)

print("---------------------")

