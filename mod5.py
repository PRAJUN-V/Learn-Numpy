import numpy as np

# Check the datatype of an array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1.dtype)

arr2 = np.array([2.3, 4.5])
print(arr2.dtype)

arr3 = np.array(['apple', 'banana', 'cherry'])
print(arr3.dtype)

# Arrays With a Defined Data Type
arr4 = np.array([1, 2, 3, 4], dtype='S')

print(arr4)
print(arr4.dtype)
