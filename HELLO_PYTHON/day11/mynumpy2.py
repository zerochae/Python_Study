import numpy as np

arr_zero = np.zeros(10)
arr_one = np.ones(10)
print(arr_zero)
print(arr_one)

arr_n = np.ones((3, 4),dtype='i')

print(arr_n)

arr_new = np.reshape(arr_n, (2, 6))
print(arr_new)
