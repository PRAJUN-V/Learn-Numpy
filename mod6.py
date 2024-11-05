# copy v/s now

import numpy as np

# The copy SHOULD NOT be affected by the changes made to the original array.
arr = np.array([1, 2, 3, 4, 5, 6])
x = np.copy(arr)

arr[0] = 10

print(arr)
print(x)

# The view SHOULD be affected by the changes made to the original array.
arr1 = np.array([1, 2, 3, 4, 5])
y = arr1.view()

arr1[0] = 43

print(arr1)
print(y)
