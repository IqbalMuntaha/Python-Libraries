import numpy as np
"""
SOAL PAKET 1
Soal 1: Membuat dan Memanipulasi Array
Buat array 1D dengan elemen dari 1 hingga 10.
Hitung jumlah dan rata-rata elemen dalam array tersebut.
Buat array 2D dari array 1D yang sudah dibuat.
Lakukan transpose pada array 2D tersebut.

Soal 2: Operasi Matematika pada Array
Buat dua array 1D masing-masing dengan elemen [1, 2, 3] dan [4, 5, 6].
Hitung elemen-wise sum dari kedua array.
Hitung elemen-wise product dari kedua array.
Hitung dot product dari kedua array.

Soal 3: Operasi Statistik pada Array
Buat array 1D dengan elemen [3, 5, 7, 9, 11].
Hitung mean, median, dan standar deviasi dari elemen array tersebut.
Temukan elemen maksimum dan minimum dalam array tersebut.

Soal 4: Indexing dan Slicing pada Array
Buat array 1D dengan elemen dari 10 hingga 20.
Ambil elemen ke-3 hingga ke-7 dari array tersebut.
Ubah elemen ke-5 dari array tersebut menjadi 100.
Ambil elemen dengan indeks genap dari array tersebut.

Soal 5: Membuat Matriks Identitas
Buat matriks identitas berukuran 3x3.
Hitung trace dari matriks identitas tersebut.
Buat matriks diagonal dengan elemen [1, 2, 3, 4].

Soal 6: Reshaping Array
Buat array 1D dengan elemen dari 1 hingga 12.
Ubah array 1D tersebut menjadi array 2D dengan ukuran 3x4.
Ubah kembali array 2D tersebut menjadi array 3D dengan ukuran 2x2x3.
"""
arr1 = np.arange (1,11)
print("1. Berikut adalah Array 1D 1-10:", arr1)
sum_arr1 = np.sum (arr1)
mean_arr1 = np.mean (arr1)
print("Jumlah:", sum_arr1)
print("Rata-rata:", mean_arr1)
print("Array 2D:\n", arr1)
arr2 = arr1.reshape (2,5)
print("Bentuk 2D reshape:\n", arr2)
transpose_arr2 = np.transpose (arr2)
print("Transpose:\n", transpose_arr2)

arr3 = np.arange(1,4)
arr4 = np.arange(4,7)
print("2 Array 1D:\n", arr3," dan ", arr4)
sum_array = arr3 + arr4
print("Wise sum: ", sum_array)
product_array = arr3 * arr4
print("Wise product: ", product_array)
dot_product = np.dot (arr3, arr4)
print("Dot product: ", dot_product)

arr5 = np.array ([3, 5, 7, 9, 11])
print("3. Array 1D: ", arr5)
mean_arr5 = np.mean (arr5)
print("Mean: ",mean_arr5)
median_arr5 = np.median (arr5)
print("Median: ", median_arr5)
standar_mediasi = np.std (arr5)
print("Standar Deviasi: ", standar_mediasi)
max_value = np.max (arr5)
print("Elemen maksimum: ", max_value)
min_value = np.min (arr5)
print("Elemen Minimum: ", min_value)

arr6 = np.arange(10,21)
print("4. Array 1D:", arr6)
subset = arr6 [2:6]
print("Subset:",subset)
arr6 [4] = 100
print("Array terbaru:", arr6)
genap = arr6 [::2]
print("Bilangan genap dari array tersebut adalah:", genap)

arr7 = np.eye(3)
print("5. Matriks identitas 3x3:\n", arr7)
trace = np.trace(arr7)
print("Trace dari matriks identitas: ",trace)
diagonal = [1,2,3,4]
diag_matrik = np.diag (diagonal)
print("Diagonal 1,2,3,4:\n", diag_matrik)

arr8 = np.arange(1,13)
print("6. Array 1D: ", arr8)
arr9 = arr8.reshape(3,4)
print("Array 2D 3x4:\n", arr9)
arr10 = arr9.reshape(2,2,3)
print("Array 3D 2X2X3:\n", arr10)