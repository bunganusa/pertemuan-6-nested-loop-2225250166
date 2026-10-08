# Pertemuan 06 Nested Loop Python

Nama: Bunga Nusa Pertiwi
NIM: 2225250166
Kelas: 3F

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan untuk membuat tabel perkalian 1 sampai n beserta statistiknya (jumlah setiap baris, total seluruh hasil, dan banyak hasil genap).

## Struktur Folder

```
pertemuan-06-nested-loop-NIM/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_pasangan_indeks.py
|   |-- 02_pola_segitiga.py
|   |-- 03_jumlah_per_baris.py
|   `-- 04_hitung_pasangan.py
`-- tugas/
    `-- tabel_perkalian_dan_statistik.py
```

## Cara Menjalankan

```
python tugas/tabel_perkalian_dan_statistik.py
```

Pada Windows, gunakan `python` sebagai pengganti `python3`. Masukkan satu bilangan bulat positif sebagai nilai n. Jika n kurang dari atau sama dengan 0, program meminta input lagi sampai valid.

## Algoritma Tugas 3

| Langkah | Aksi | Kode |
| --- | --- | --- |
| 1 | Baca n dan validasi sampai positif | `while n <= 0:` |
| 2 | Siapkan akumulator keseluruhan dan counter sebelum kedua loop | `total_semua = 0`, `count_genap = 0` |
| 3 | Loop luar mengatur baris ke-i | `for i in range(1, n + 1):` |
| 4 | Reset akumulator per baris di awal setiap baris | `total_baris = 0` |
| 5 | Loop dalam mengatur kolom ke-j | `for j in range(1, n + 1):` |
| 6 | Hitung dan cetak hasil di baris yang sama | `hasil = i * j`, `print(..., end="")` |
| 7 | Tambahkan hasil ke kedua akumulator | `total_baris += hasil`, `total_semua += hasil` |
| 8 | Hitung hasil genap | `if hasil % 2 == 0: count_genap += 1` |
| 9 | Setelah loop dalam, tampilkan jumlah baris dan pindah baris | `print(f" | jumlah baris = {total_baris}")` |
| 10 | Setelah kedua loop, tampilkan statistik keseluruhan | `print(total_semua)`, `print(count_genap)` |

Peran setiap bagian:

| Bagian | Peran |
| --- | --- |
| Loop luar (`i`) | Mengatur baris tabel |
| Loop dalam (`j`) | Mengatur kolom pada setiap baris |
| `total_baris` | Akumulator per baris, direset di setiap iterasi loop luar |
| `total_semua` | Akumulator keseluruhan, dibuat sekali sebelum kedua loop |
| `count_genap` | Counter, bertambah 1 hanya ketika `hasil` genap |

## Hasil Pengujian

| n | Jumlah pasangan | Total semua (diharapkan) | Genap (diharapkan) | Total semua (aktual) | Genap (aktual) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 0 | 1 | 0 | Sesuai |
| 2 | 4 | 9 | 3 | 9 | 3 | Sesuai |
| 3 | 9 | 36 | 5 | 36 | 5 | Sesuai |

Jumlah setiap baris untuk n = 3:

| Baris i | Hasil perkalian | Jumlah baris (aktual) | Status |
| --- | --- | --- | --- |
| 1 | 1, 2, 3 | 6 | Sesuai |
| 2 | 2, 4, 6 | 12 | Sesuai |
| 3 | 3, 6, 9 | 18 | Sesuai |

Pengujian validasi:

| Input | Hasil | Status |
| --- | --- | --- |
| 0 | Ditolak, muncul pesan "n harus positif." | Sesuai |
| -2 | Ditolak, muncul pesan "n harus positif." | Sesuai |
| 3 (setelah input tidak valid) | Program berlanjut dan menampilkan tabel | Sesuai |

### Tracing untuk n = 2

| i | j | hasil = i * j | total_baris sesudah | total_semua sesudah | count_genap sesudah |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 | 0 |
| 1 | 2 | 2 | 3 | 3 | 1 |
| 2 | 1 | 2 | 2 | 5 | 2 |
| 2 | 2 | 4 | 6 | 9 | 3 |

Pada baris i = 2, `total_baris` kembali mulai dari 0 (menjadi 2 setelah pasangan pertama), sedangkan `total_semua` terus bertambah dari 3 menjadi 5. Ini menunjukkan perbedaan akumulator per baris dan akumulator keseluruhan.

Cara membuktikan `count_genap` benar: untuk n = 3, hasil perkalian adalah 1, 2, 3, 2, 4, 6, 3, 6, 9. Bilangan genapnya adalah 2, 2, 4, 6, 6, yaitu 5 buah, sama dengan keluaran program.

## Analisis Efisiensi

Badan loop dalam (termasuk `hasil = i * j`) dieksekusi n x n = n² kali.

| n | Iterasi loop luar | Iterasi loop dalam per baris | Total eksekusi badan loop dalam |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 3 | 3 | 3 | 9 |
| 10 | 10 | 10 | 100 |
| 100 | 100 | 100 | 10.000 |

Tabel, jumlah baris, total keseluruhan, dan counter genap dihitung dalam satu kali lintasan nested loop, jadi tidak ada loop tambahan atau perhitungan yang diulang. Bagian yang paling banyak melakukan operasi ketika n membesar adalah badan loop dalam, karena jumlah eksekusinya tumbuh sebanding n².

## Refleksi

| Kesalahan nested loop | Akibat | Perbaikan |
| --- | --- | --- |
| `total_baris = 0` ditaruh di dalam loop dalam | Total direset pada setiap pasangan, jumlah baris hanya mencerminkan nilai terakhir | Pindahkan ke dalam loop luar, sebelum loop dalam |
| `total_semua = 0` ditaruh di dalam loop luar | Total keseluruhan ikut direset di setiap baris, hasil akhir salah | Buat sekali saja sebelum kedua loop |


## Sumber dan Bantuan

| Sumber | Keterangan |
| --- | --- |
| Modul Pertemuan 6 Algoritma dan Pemrograman | Bagian Tugas 3 dan Solusi Ringkas Tugas 3, Prodi S1 Pendidikan Matematika FKIP Untirta |
| Bantuan AI (Claude) | Membantu menyusun kode, README, dan penjelasan. Seluruh bagian telah dipelajari dan dapat dijelaskan oleh pemilik repositori |