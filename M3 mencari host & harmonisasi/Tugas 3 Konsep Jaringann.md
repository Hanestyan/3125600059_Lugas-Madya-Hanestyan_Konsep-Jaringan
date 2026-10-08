**TUGAS**

**KONSEP JARINGAN**

**MENCARI HOST PERTAMA & TERAKHIR**



Nama : Lugas Madya Hanestyan

NRP : 3125600059

Dosen Pengajar : Dr Ferry Astika Saputra ST, M.Sc

**PROGRAM STUDI D4 TEKNIK INFORMATIKA**

**POLITEKNIK ELEKTRONIKA NEGERI SURABAYA (PENS)**

**TAHUN 2026**

1. **TUGAS**

Cari ip gateway, host pertama, host terakhir, broadcast, ip network

1. 21.26.8.5
2. 212.6.8.3
3. 103.24.56.32
4. 1.1.1.1
5. 172.31.16.8

Dan buat pyhton harmonisasi dari 1.3.5.7.9.10

1. **PEMBAHASAN**

| **Alamat IP** | **Kelas** | **Rentang Kelas** | **IP Network** | **Host Pertama** | **Host Terakhir** | **Broadcast** |
| --- | --- | --- | --- | --- | --- | --- |
| 21.26.8.5 | Kelas A | 1 – 126 | 21.0.0.0 | 21.0.0.1 | 21.255.254 | 21.255.255.255 |
| 212.6.8.3 | Kelas C | 192 – 223 | 212.6.8.0 | 212.6.8.1 | 212.6.8.254 | 212.6.8.255 |
| 103.24.56.32 | Kelas A | 1 – 126 | 103.0.0.0 | 103.0.0.1 | 103.255.255.254 | 103.255.255.255 |
| 1.1.1.1 | Kelas A | 1 – 126 | 1.0.0.0 | 1.0.0.1 | 1.255.255.254 | 1.255.255.255 |
| 172.31.16.8 | Kelas B | 128 – 191 | 172.0.0.0 | 172.0.0.1 | 172.255.255.254 | 172.255.255.255 |

Script Python Harmonisasi dari 1.3.5.7.9.10

**Input:**

import numpy as np

import matplotlib.pyplot as plt

_\# Deret frekuensi ganjil untuk membentuk square wave_

frekuensi\_ganjil = \[1, 3, 5, 7, 9\]

t = np.linspace(0, 2, 1000)

sinyal\_gabungan = np.zeros(len(t))

plt.figure(_figsize_\=(12, 6))

_\# Proses harmonisasi berdasarkan Deret Fourier_

for f in frekuensi\_ganjil:

    _\# Pada deret Fourier untuk gelombang kotak, amplitudonya adalah 1/f_

    amplitudo = 1 / f

    gelombang = amplitudo \* np.sin(2 \* np.pi \* f \* t)

    sinyal\_gabungan += gelombang

_\# Menggambar garis tipis untuk melihat setiap gelombang sinus yang ditambahkan_

    plt.plot(t, sinyal\_gabungan, _linestyle_\=':', _alpha_\=0.5, _label_\=f'Ditambah frekuensi {f}Hz')

_\# Menggambar hasil akhir yang sudah mendekati bentuk kotak_

plt.plot(t, sinyal\_gabungan, _color_\='red', _linewidth_\=2.5, _label_\='Hasil Akhir (Mendekati Square Wave)')

plt.title('Harmonisasi Frekuensi Ganjil Membentuk Square Wave', _fontsize_\=14)

plt.xlabel('Waktu (detik)', _fontsize_\=12)

plt.ylabel('Amplitudo', _fontsize_\=12)

plt.legend(_loc_\='upper right')

plt.grid(True, _linestyle_\='--', _alpha_\=0.7)

plt.axhline(0, _color_\='black', _linewidth_\=1)

plt.show()

**Output:**



**Cara kerja :**

- -   Skrip memulai dengan gelombang sinus dasar berfrekuensi 1 Hz. Bentuknya masih melengkung halus.
    - Saat frekuensi 3 Hz ditambahkan, puncak gelombang mulai sedikit mendatar.
    - Saat frekuensi 5, 7, dan 9 Hz ditambahkan, lekukan-lekukan gelombang sinus semakin saling menghilangkan di bagian puncak, membuat bagian atas dan bawah grafik semakin datar dan transisinya (garis naik-turun) semakin tegak lurus.
    - Jika deret ganjil ini diteruskan sampai tak terhingga (misal sampai 99 atau 1001), grafiknya akan menjadi square wave bersudut 90 derajat yang sempurna.
