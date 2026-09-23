import numpy as np
import time

# list_data = [1, 2, 3, 4, 5]
# np_data = np.array([1, 2, 3, 4, 5])
# print(list_data, type(list_data))
# print(np_data, type(np_data))

# import numpy as np

# # 예시 1: 리스트는 +연산 시 이어붙이기(concat)가 됨
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(list1 + list2)  # 결과: [1, 2, 3, 4, 5, 6] (합쳐짐)

# # 예시 2: 넘파이 배열은 +연산 시 원소별 덧셈이 됨
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# print(arr1 + arr2)  # 결과: [5 7 9] (같은 위치끼리 더해짐)

# # 예시 3: 리스트로 원소별 덧셈을 하려면 반복문이 필요함
# result = []
# for i in range(len(list1)):
#     result.append(list1[i] + list2[i])
# print(result)  # 결과: [5, 7, 9]

# # 예시 4: 넘파이는 대용량 데이터 처리 속도가 훨씬 빠름

# big_list = list(range(1000000))
# big_arr = np.arange(1000000)

# start = time.time()
# big_list_result = [x * 2 for x in big_list]
# print("리스트 연산 시간:", time.time() - start)

# start = time.time()
# big_arr_result = big_arr * 2
# print("넘파이 연산 시간:", time.time() - start)

li = list()
start = time.time()
for i in range(1000000):
    li.append(0)
print("list append 연산 시간:", time.time() - start)

arr = np.array([])
start = time.time()
for i in range(1000000):
    np.append(arr, 0)
print("ndarray append 연산 시간:", time.time() - start)