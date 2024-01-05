import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 5

# Mengelompokkan tinggi badan ke dalam interval tertentu
min_height = min(tinggi_badan)
max_height = max(tinggi_badan)
intervals = np.arange(min_height, max_height + interval_size, interval_size)

# Menghitung frekuensi tinggi badan dalam interval
frekuensi = [
    len([x for x in tinggi_badan if interval[0] <= x < interval[1]])
    for interval in zip(intervals, intervals[1:])
]

# Visualisasi data dalam bentuk histogram
plt.figure(figsize=(5, 4))
plt.hist(tinggi_badan, bins=intervals, color="blue", alpha=0.5, density=True)

# Menghitung asumsi distribusi normal dengan rata-rata dan standar deviasi
sample_mean = np.mean(tinggi_badan)
sample_std = np.std(tinggi_badan)

# Menentukan distribusi normal dari hasil operasi di atas
dist = norm(sample_mean, sample_std)

# Menambahkan kurva pdf pada hasil visualisasi data
values = np.linspace(min_height, max_height, 100)
probabilitas = dist.pdf(values)
plt.plot(values, probabilitas, "r-", linewidth=2)

plt.title("Histogram Frekuensi Tinggi Badan")
plt.xlabel("Tinggi Badan (cm)")
plt.ylabel("Frekuensi")
plt.show()
