# fungsi_gabungan.py

# Fungsi Rekursif untuk Menghitung Faktorial
def faktorial(n):
    # Kondisi dasar: jika n adalah 1, kembalikan 1
    if n == 1:
        return 1
    # Panggil kembali fungsi faktorial dengan n-1
    else:
        return n * faktorial(n - 1)

# Fungsi Biasa untuk Menambahkan Dua Angka
def tambah(a, b):
    return a + b

# Fungsi Rekursif untuk Menghitung Fibonacci
def fibonacci(n):
    # Kondisi dasar: jika n adalah 0 atau 1, kembalikan n
    if n <= 1:
        return n
    # Panggil kembali fungsi fibonacci dengan n-1 dan n-2
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Fungsi Biasa untuk Menghitung Luas Persegi Panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Contoh Penggunaan Fungsi-fungsi di Atas

# Faktorial
angka_faktorial = 5
print(f"Faktorial dari {angka_faktorial} adalah {faktorial(angka_faktorial)}")

# Penjumlahan
angka1 = 3
angka2 = 7
print(f"Hasil penjumlahan {angka1} dan {angka2} adalah {tambah(angka1, angka2)}")

# Fibonacci
urutan_fibonacci = 6
print(f"Fibonacci ke-{urutan_fibonacci} adalah {fibonacci(urutan_fibonacci)}")

# Luas Persegi Panjang
panjang = 10
lebar = 5
print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas_persegi_panjang(panjang, lebar)}")
