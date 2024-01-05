import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

# TODO 1: Ekstrak harga produk dan jumlah produk terjual untuk visualisasi pertama
harga_produk = [harga for _, harga, _ in data_transaksi]
jumlah_terjual = [jumlah for _, _, jumlah in data_transaksi]

# TODO 2: Buat scatter plot untuk hubungan antara harga produk dan jumlah produk terjual
plt.figure(figsize=(10, 5))
plt.scatter(harga_produk, jumlah_terjual, color="blue", label="Jumlah Terjual")
plt.title("Hubungan Antara Harga dan Jumlah Produk Terjual")
plt.xlabel("Harga Produk")
plt.ylabel("Jumlah Terjual")
plt.legend()
plt.grid(True)
plt.show()

# TODO 3: Hitung total pendapatan untuk setiap produk
pendapatan_produk = list(map(lambda x: x[1] * x[2], data_transaksi))

# TODO 4: Tambahkan bar chart untuk menyajikan pendapatan produk
produk_nama = [produk for produk, _, _ in data_transaksi]

plt.figure(figsize=(10, 5))
plt.bar(produk_nama, pendapatan_produk, color="green", label="Pendapatan")
plt.title("Pendapatan Produk")
plt.xlabel("Produk")
plt.ylabel("Pendapatan")
plt.legend()
plt.show()
