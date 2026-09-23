import numpy as np

arr1 = np.array([1, 2, 3])
print(arr1)
print()

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6 ]
])
print(arr2)
print()

arr3 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr3)
print()

arr4 = np.array([1, 2, 3], dtype = np.float64)
print(arr4)
print()

arr5 = np.array((10, 20, 30))
print(arr5)
print()

print(np.zeros((2, 3)))
print()

print(np.ones((3, 2)))
print()

print(np.full((2, 2), 7))
print()

print(np.arange(0, 10, 2))
print()

print(np.linspace(0, 1, 5))
print()

print(np.eye(3))
print()

print(np.random.rand(2, 2))
print()

print(np.random.randint(1, 10, size = 5))
print()

print(np.random.random())
print()

print(np.random.random(10))
print()

print(np.random.rand(2, 2) * 10)
print()

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(arr)
print("shape:", arr.shape)
print("ndim:", arr.ndim)
print("dtype:", arr.dtype)
print("size:", arr.size)

arr1d = np.array([1, 2, 3, 4])
print(arr1d.shape)

arr3d = np.zeros((2, 3, 4))
print(arr3d.shape)

arr = np.array([1, 2, 3])
arr_float = arr.astype(np.float64)
print(arr_float)

arr2 = np.array([1.7, 2.3, 3.9])
arr_int = arr2.astype(np.int32)
print(arr_int)

arr3 = np.array([1, 2, 3])
arr_str = arr3.astype(str)
print(arr_str)

arr4 = np.array([0, 1, 2, -1])
arr_bool = arr4.astype(bool)
print(arr_bool)

arr = np.array([10, 20, 30, 40, 50])
arr2d = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr[0])
print(arr[-1])
print()

print(arr2d[0, 2])
print(arr2d[1, 2])
print()

print(arr[1:4])
print(arr[:3])
print(arr[::2])
print()

print(arr2d[0:2, 1:3])
print()

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(arr2[:,:2])
print()

arr = np.array([10, 20, 30, 40, 50])
print(arr[[0, 2, 4]])
print()

scores = np.array([55, 90, 78, 45, 88, 92, 60])

print(scores >= 60)
print()

print(scores[scores >= 60])
print()

print(arr[arr > 20])
print()

print(arr[(arr > 10) & (arr < 50)])
print()

arr[0] = 100
print(arr)