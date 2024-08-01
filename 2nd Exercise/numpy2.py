import numpy as np
import matplotlib.pyplot as plt

#Membuat datanya terlebih dahulu
np.random.seed (7)
data_penjualan = np.random.randint (400, 1500, size=(12,5))

#Membuat analisis statistik
total_penjualan = data_penjualan.sum(axis=0)
rata_penjualan = data_penjualan.mean(axis=0)
penjualan_tertinggi = np.argmax(data_penjualan, axis=0)
penjualan_terendah = np.argmin(data_penjualan, axis=0)
standar_deviasi = data_penjualan.std(axis=0)

#Membuat perbandingan dan insight
cabang_tertinggi = np.argmax(penjualan_tertinggi)
cabang_terendah = np.argmin(penjualan_terendah)
selisih_rata_penjualan = rata_penjualan[cabang_tertinggi] - rata_penjualan[cabang_terendah]

#Mencari cabang dengan variabilitas tertinggi dan terendah
variabilitas_tertinggi = np.argmax(standar_deviasi)
variabilitas_terendah = np.argmin(standar_deviasi)

#Visualisasi data penjualan per bulan untuk tiap cabang
bulan = np.arange(1,13)
for i in range(data_penjualan.shape[1]):
    plt.plot(bulan, data_penjualan[:,i], label=f'Cabang {i + 1}')

plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')
plt.title('Penjualan Bulanan per Cabang')
plt.legend()
plt.grid(True)
plt.show()

#Visualisasi total penjualan antar cabang
plt.bar(np.arange(1,6), total_penjualan, color=['yellow','red','blue','#C8A2C8','green'])
plt.xlabel('Cabang')
plt.ylabel('Jumlah Penjualan')
plt.title('Total Penjualan Antar Cabang')
plt.xticks(np.arange(1,6), [f'Cabang {i}'for i in range(1,6)])
plt.show()

#Hasil analisa
print("Data penjualan setahun untuk 5 cabang toko:\n", data_penjualan)
print("Total penjualan per cabang:\n", total_penjualan)
print("Rata-rata penjualan tiap cabang:\n", rata_penjualan)
print("Bulan dengan penjualan tertinggi tiap cabang:\n", penjualan_tertinggi + 1)
print("Bulan dengan penjualan terendah tiap cabang:\n", penjualan_terendah + 1)
print("Standar deviasi perbulan tiap cabang:\n", standar_deviasi)
print("Perbandingan total penjualan antar cabang (tertinggi):\n", cabang_tertinggi)
print("Perbandingan total penjualan antar cabang (terendah):\n", cabang_terendah)
print("Selisih rata-rata penjualan antar cabang antara tertinggi dengan terendah:\n", selisih_rata_penjualan)
print("Cabang dengan variabilitas tertinggi:\n", variabilitas_tertinggi)
print("Cabang dengan variabilitas terendah:\n", variabilitas_terendah)