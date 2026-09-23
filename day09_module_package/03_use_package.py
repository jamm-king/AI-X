# from shop import product
# from shop import cart

# price1 = product.get_price("사과")
# price2 = product.get_price("바나나")

# print(price1, price2)
# print(cart.total([price1, price2]))

# Student 객체를 생성하고 사용해보세요.
# from school.student import Student

# s = Student(
#     name = "홍길동",
#     age = 20
# )
# s.info()

# StudentScore 객체를 생성하고 사용해보세요.
from school.student_score import StudentScore

score = StudentScore(
    kor = 80,
    eng = 90,
    math = 85
)
print(score.show_total())