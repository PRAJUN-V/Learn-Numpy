# The shape of an array is the number of elements in each dimension.

import numpy as np

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr1.shape)


arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
newArr = arr2.reshape(3, 3) # reshape will create new array with the given shape.
print(newArr)

arr2.resize(3, 3) # resize will reshape the existing array  itself without new array.
print(arr2)

# Flattening the array
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

