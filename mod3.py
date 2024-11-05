import numpy as np

# access array elements using  index
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1[0])

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2[1][2])
# negative indexing
print(arr2[-1])
