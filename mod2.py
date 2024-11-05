import numpy as np

# 0d array
arr1 = np.array(1)

# 1d array
arr2 = np.array([1, 2])

# 2d array
arr3 = np.array([[1, 2, 3], [4, 5, 6]])

# 3d array
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# Check dimension
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
print(arr4.ndim)

# When the array is created, you can define the number of dimensions by using the ndmin argument.
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)
print(arr5.ndim)
