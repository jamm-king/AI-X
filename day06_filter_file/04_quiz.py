scores_data = [78, 92, 55, 88, 63, 40, 95, 70]
fruits = ["apple", "banana", "kiwi", "fig", "watermelon", "pear"]
words = ["Hello", "World", "Python", "Pandas", "Numpy"]

# - -- map() 연습 ---
# 1. scores_data의 각 점수에 5점씩 가산점을 더한 리스트를 만들어 보세요. (map 사용)
# 2. scores_data의 각 점수를 "OO점"과 같은 문자열 형태로 바꾼 리스트를 만들어 보세요. (map 사용)
# 3. fruits의 각 단어를 모두 대문자로 바꾼 리스트를 만들어 보세요. (map 사용)
# 4. words의 각 단어의 길이(글자 수)로 이루어진 리스트를 만들어 보세요. (map 사용)

plus_five = list(map(lambda n: n + 5, scores_data))
print(plus_five)
scores_str = list(map(lambda n: str(n) + "점", scores_data))
print(scores_str)
fruits_upper = list(map(lambda fruit: fruit.upper(), fruits))
print(fruits_upper)
length_words = list(map(len, words))
print(length_words)

# - -- filter() 연습 ---
# 1. scores_data 중에서 70점 이상인 점수만 걸러내 보세요. (filter 사용)
# 2. scores_data 중에서 60점 미만(과락)인 점수만 걸러내 보세요. (filter 사용)
# 3. fruits 중에서 이름의 길이가 5글자 이상인 과일만 걸러내 보세요. (filter 사용)
# 4. fruits 중에서 "a"가 포함된 과일만 걸러내 보세요. (filter 사용)

high_scores = list(filter(lambda n: n >= 70, scores_data))
print(high_scores)
low_scores = list(filter(lambda n: n < 60, scores_data))
print(low_scores)
long_fruits = list(filter(lambda fruit: len(fruit) >= 5, fruits))
print(long_fruits)
a_fruits = list(filter(lambda fruit: "a" in fruit, fruits))
print(a_fruits)

# - -- map + filter 함께 사용 ---
# 1. scores_data 중 70점 이상인 점수만 걸러낸 뒤, 그 점수들에 각각 10%를 가산한 리스트를 만들어 보세요.
# (filter로 먼저 거르고, 그 결과를 map으로 가공)
# 2. words 중에서 길이가 5글자 이상인 단어만 걸러낸 뒤, 모두 소문자로 바꾼 리스트를 만들어 보세요.

processed_scores = list(
    map(
        lambda score: score + score / 10.0,
        filter(
            lambda score: score >= 70,
            scores_data
        )
    )
)
print(processed_scores)

processed_words = list(
    map(
        lambda word: word.lower(),
        filter(
            lambda word: len(word) >= 5,
            words
        )
    )
)
print(processed_words)