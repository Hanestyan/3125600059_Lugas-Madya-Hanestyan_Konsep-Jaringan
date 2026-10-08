import numpy as np
import matplotlib.pyplot as plt

# Deret frekuensi ganjil untuk membentuk square wave
frekuensi_ganjil = [1, 3, 5, 7, 9]

t = np.linspace(0, 2, 1000)
sinyal_gabungan = np.zeros(len(t))

plt.figure(figsize=(12, 6))

# Proses harmonisasi berdasarkan Deret Fourier
for f in frekuensi_ganjil:
    # Pada deret Fourier untuk gelombang kotak, amplitudonya adalah 1/f
    amplitudo = 1 / f 
    gelombang = amplitudo * np.sin(2 * np.pi * f * t)
    sinyal_gabungan += gelombang
    
    # Menggambar garis tipis untuk melihat setiap gelombang sinus yang ditambahkan
    plt.plot(t, sinyal_gabungan, linestyle=':', alpha=0.5, label=f'Ditambah frekuensi {f}Hz')

# Menggambar hasil akhir yang sudah mendekati bentuk kotak
plt.plot(t, sinyal_gabungan, color='red', linewidth=2.5, label='Hasil Akhir (Mendekati Square Wave)')

plt.title('Harmonisasi Frekuensi Ganjil Membentuk Square Wave', fontsize=14)
plt.xlabel('Waktu (detik)', fontsize=12)
plt.ylabel('Amplitudo', fontsize=12)
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=1)

plt.show()