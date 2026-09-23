"""
 코드 작성 퀴즈 (10문제)
"""
import numpy as np
"""
1번. 1, 2, 3을 담은 넘파이 1차원 배열을 만들고 출력하세요.
"""
arr = np.array([1, 2, 3])
print("### 1 ###")
print(arr)

"""
2번. 1로 채워진 2x2 크기의 배열을 만드세요. (힌트: np.ones)
"""
arr = np.ones((2, 2))
print("### 2 ###")
print(arr)

"""
3번. 5라는 값으로 채워진 3x3 배열을 만드세요. (힌트: np.full)
"""
arr = np.full((3, 3), 5)
print("### 3 ###")
print(arr)

"""
4번. 0부터 20 전까지 5씩 증가하는 배열을 만드세요. (힌트: np.arange)
"""
arr = np.arange(0, 20, 5)
print("### 4 ###")
print(arr)

"""
5번. 아래 배열의 shape, ndim, dtype을 각각 출력하세요.
arr = np.array([[1, 2], [3, 4], [5, 6]])
"""
arr = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
print("### 5 ###")
print(f"shape: {arr.shape}")
print(f"ndim: {arr.ndim}")
print(f"dtype: {arr.dtype}")

"""
6번. 아래 정수형 배열을 실수형(float64)으로 변환하여 출력하세요.
arr = np.array([1, 2, 3])
"""
arr = np.array([1, 2, 3])
arr_float = arr.astype(np.float64)
print("### 6 ###")
print(arr_float)

"""
7번. 아래 배열에서 인덱스 0, 2, 4에 해당하는 값만 팬시 인덱싱으로 뽑아 출력하세요.
arr = np.array([10, 20, 30, 40, 50])
"""
arr = np.array([10, 20, 30, 40, 50])
print("### 7 ###")
print(arr[[0, 2, 4]])

"""
8번. 아래 배열에서 60 이상인 값만 불린 인덱싱으로 뽑아 출력하세요.
scores = np.array([55, 90, 78, 45, 88, 92, 60])
"""
scores = np.array([55, 90, 78, 45, 88, 92, 60])
print("### 8 ###")
print(scores[scores >= 60])

"""
9번. 아래 2차원 배열에서 슬라이싱을 이용해 모든 행의 첫 번째 열만 출력하세요.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
"""
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print("### 9 ###")
print(arr[:, :1])

"""
10번. 아래 배열에서 인덱스 0번 값을 100으로 수정한 뒤 배열 전체를 출력하세요.
arr = np.array([10, 20, 30, 40, 50])
"""
arr = np.array([10, 20, 30, 40, 50])
arr[0] = 100
print("### 10 ###")
print(arr)
