import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])

arr1 = np.array([1, 2, 3, 4, 5])
print("Array ID:", arr1)

arr2 = np.array([1, 2, 3, 4])
print("Array 2D:\n", arr2)

sum_arr1 = np.sum(arr1)
print("Jumlah elemen arr1:", sum_arr1)

transpose_arr2 = np.array(arr2)
print("Tranpose arr2\n", transpose_arr2)

transpose_matrix = np.transpose(matrix)
print("Transpose Matrix\n", transpose_matrix)
