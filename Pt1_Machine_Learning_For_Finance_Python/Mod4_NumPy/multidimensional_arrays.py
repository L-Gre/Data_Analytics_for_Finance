# module = collection of functions
# package / library = collection of modules

import numpy as np

# simple array
array_1 = np.array([1, 2, 3, 4, 5])
print(array_1)
type(array_1)

# numpy auto-transforms entries: auto-transformation to string
array_2 = np.array([1, 2, 'three', 4, 5])
print(array_2)

# auto-transform to float
array_3 = np.array([1, 2, 3.0, 4, 5])
print(array_3)


# multi-dimensional arrays

# You can create multi-dimensional arrays using NumPy, i.e. lists of lists --> table w columns and rows

array_4 = np.array([[1, 2, 3] , [4, 5, 6]])
print(array_4)
array_4.shape


# Exercise

import numpy as np

array_5 = np.array([[1, 2] , [3, 4] , [5, 6]])
print(array_5)
print('---')
print(array_5.shape)

# .reshape() and .transpose()

print(array_5.reshape(2, 3))
print(array_5.transpose())