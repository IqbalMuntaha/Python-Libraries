"""
SOAL PAKET 1.2
Soal 1: Pembuatan dan Operasi Dasar pada Array
Buat array 1D dengan elemen dari 10 hingga 25.
Hitung elemen-wise sum antara array tersebut dengan array lain yang berisi angka dari 25 hingga 40.
Hitung elemen-wise product antara kedua array tersebut.
Soal 2: Manipulasi Array
Buat matriks 2D berukuran 4x4 dengan elemen dari 1 hingga 16.
Hitung transpose dari matriks tersebut.
Hitung trace dari matriks tersebut.
Reshape matriks tersebut menjadi array 1D dan tampilkan hasilnya.
Soal 3: Matriks Identitas dan Matriks Diagonal
Buat matriks identitas berukuran 4x4.
Hitung trace dari matriks identitas tersebut.
Buat matriks diagonal dengan elemen [5, 6, 7, 8, 9].
Tambahkan matriks identitas 4x4 dengan matriks diagonal yang Anda buat.
Soal 4: Dot Product
Buat dua vektor 1D, a dan b, masing-masing berukuran 5, dengan elemen dari 1 hingga 5 dan dari 6 hingga 10.
Hitung dot product dari kedua vektor tersebut.
Buat dua matriks 2D, A dan B, masing-masing berukuran 3x3 dengan elemen dari 1 hingga 9 dan dari 10 hingga 18.
Hitung dot product dari kedua matriks tersebut.
Soal 5: Reshaping Array
Buat array 1D dengan elemen dari 1 hingga 16.
Ubah array 1D tersebut menjadi array 2D dengan ukuran 4x4.
Ubah kembali array 2D tersebut menjadi array 3D dengan ukuran 2x2x4.
Soal 6: Pengindeksan dan Pemotongan Array
Buat matriks 2D berukuran 5x5 dengan elemen dari 1 hingga 25.
Ambil submatriks 3x3 dari matriks tersebut yang dimulai dari elemen (2,2).
Ubah elemen di submatriks tersebut menjadi 0.
Tampilkan matriks 2D yang sudah diubah.
"""
import numpy as np

arr1 = np.arange (10,26)
arr2 = np.arange (25,41)
print("1. Array: ", arr1)
print("Array 2", arr2)
wisesum = np.add (arr1,arr2)
print("Wise-sum:", wisesum)
wiseproduct = np.multiply (arr1,arr2)
print("Wise-product:", wiseproduct)

arr3 = np.arange (1,17)
arr4 = arr3.reshape (4,4)
print("2. Matriks 2D 4x4:\n",arr4)
transpose_2 = np.transpose (arr4)
print("Transpose:\n",transpose_2)
trace = np.trace (arr4)
print("Trace:", trace)
arr5 = arr4.reshape (-1)
print("Reshape Array 1D:\n", arr5)

identitas = np.eye (2*2)
print("3. Matriks Identitas:\n", identitas)
trace_iden = np.trace (identitas)
print("Trace:", trace_iden)
diag = np.diag ([5,6,7,8])
print("Matriks diagonal:\n", diag)
tambahkan = identitas + diag
print("Tambahkan matriks 4x4 dengan matriks diagonal:\n", tambahkan)

arrA = np.arange(1,6)
arrB = np.arange(6,11)
WProduct = np.multiply(arrA,arrB)
DProduct = np.dot (arrA,arrB)
print("4. Berikut adalah 2 Array tersebut\nA. Array A:",arrA,"\nB. Array B:",arrB)
print("Wise-product:",WProduct)
print("Dot dari kedua array:",DProduct)
matA = np.arange(1,10)
matAres = matA.reshape(3,3)
matB = np.arange(10,19)
matBres = matB.reshape(3,3)
print ("Matrik 3X3 A:\n", matAres,"\nMatrik 3x3 B:\n",matBres)
WProductMatAB = np.multiply(matAres,matBres)
print ("Wise product Array 2D:\n", WProductMatAB)
DProductMatAB = np.dot (matAres,matBres)
print("Dot Product Array 2D:\n", DProductMatAB)

arr6 = np.arange(1,17)
print("5. Array 1D: ",arr6)
arr7 = arr6.reshape(4,4)
print("Array 2D 4x4:\n",arr7)
arr8 = arr7.reshape(2,2,4)
print("Array 3D 2x2x4:\n", arr8)

arr9 = np.arange(1,26)
arr10 = arr9.reshape(5,5)
print("6. Matriks 2D 5x5:\n", arr10)
submatrik = arr10 [2:5, 2:5]
print("Submatrik 3x3 dimulai dari elemen (2,2):\n",submatrik)
arr10[2:5,2:5] = [[0,0,0],[0,0,0],[0,0,0]]
print("Rubah submatrik menjadi 0:\n",arr10)
print("Hanya rubah isi submatrik menjadi 0:\n", submatrik)
