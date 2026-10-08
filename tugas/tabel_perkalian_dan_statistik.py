"""
Tugas 3: Tabel Perkalian dan Statistik
Pertemuan 06 - Nested Loop, Pola, Akumulasi, dan Pencacahan

Program membentuk tabel perkalian 1 sampai n, lalu menghitung:
- jumlah setiap baris (akumulator per baris)
- total seluruh hasil perkalian (akumulator keseluruhan)
- banyak hasil yang genap (counter)
"""

print("Tabel Perkalian dan Statistik")

# 1. Baca n, lalu validasi dengan while sampai n positif
n = int(input("n: "))
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# 2. Inisialisasi di luar kedua loop karena nilainya mencakup seluruh tabel
total_semua = 0   # akumulator keseluruhan (tidak boleh direset)
count_genap = 0   # counter hasil genap

# 3. Loop luar: mengatur baris ke-i
for i in range(1, n + 1):
    total_baris = 0   # akumulator per baris: direset di awal setiap baris

    # 4. Loop dalam: mengatur kolom ke-j pada baris ke-i
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")   # cetak satu sel, tetap di baris yang sama

        total_baris += hasil          # akumulasi per baris
        total_semua += hasil          # akumulasi keseluruhan

        if hasil % 2 == 0:            # pencacahan: hanya jika hasil genap
            count_genap += 1

    # 5. Setelah loop dalam selesai: tampilkan jumlah baris, pindah baris
    print(f" | jumlah baris = {total_baris}")

# 6. Setelah kedua loop selesai: tampilkan statistik keseluruhan
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")