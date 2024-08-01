import numpy as np
import matplotlib.pyplot as plt

np.random.seed (7)
data_penjualan = np.random.randint(100,250, size=(12,5))

total_penjualan = data_penjualan.sum (axis=0)
rata_penjualan = data_penjualan.mean (axis=0)
penjualan_tertinggi = np.argmax(data_penjualan, axis=0)
penjualan_terendah = np.argmin (data_penjualan)

produk_jual_tertinggi = np.argmax(total_penjualan)
produk_jual_terendah = np.argmin(total_penjualan)

selisih_rata = rata_penjualan[produk_jual_tertinggi] - rata_penjualan[produk_jual_terendah]

print("Data Penjualan Setahun UNIPMA MART:\n", data_penjualan)
print("Berikut total penjualan per produk:\n", total_penjualan)
print("Berikut rata-rata per bulan setiap produk:\n", rata_penjualan)
print("Bulan dengan penjualan tertinggi setiap produk adalah:\n", penjualan_tertinggi + 1)
print("Bulan dengan penjualan terendah setiap produk adalah:\n", penjualan_terendah + 1)
print("Produk dengan penjualan tertinggi adalah: ",penjualan_tertinggi)
print("Produk dengan penjualan terendah adalah: ",produk_jual_terendah)
print("Selisih rata-rata penjualan adalah: ",selisih_rata)

bulan = np.arange(1, 13)
for i in range(data_penjualan.shape[1]):
    plt.plot(bulan, data_penjualan[:, i], label=f'Produk {i + 1}')

plt.xlabel('Bulan')
plt.ylabel('Jumlah Penjualan')
plt.title('Penjualan Produk per Bulan')
plt.legend()
plt.grid(True)
plt.show()