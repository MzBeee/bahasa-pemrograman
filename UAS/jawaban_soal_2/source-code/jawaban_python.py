# fungsi_exception_handling.py

def konversi_angka(angka_str):
    try:
        # Usahakan melakukan konversi string menjadi integer
        angka = int(angka_str)
    except ValueError:
        # Tangani kesalahan jika string tidak bisa dikonversi menjadi integer
        print("Error: Input harus berupa string yang dapat dikonversi menjadi integer.")
        return None
    except TypeError:
        # Tangani kesalahan jika argumen bukan string
        print("Error: Argumen harus berupa string.")
        return None
    else:
        # Jika tidak ada kesalahan, kembalikan hasil konversi
        return angka
    finally:
        # Blok ini selalu dijalankan, baik ada kesalahan atau tidak
        print("Eksekusi blok finally.")

# Pengujian Fungsi

# Pengujian kasus konversi string valid
print("Hasil konversi '123' adalah:", konversi_angka('123'))

# Pengujian kasus string yang tidak bisa dikonversi
print("Hasil konversi 'abc' adalah:", konversi_angka('abc'))

# Pengujian kasus dengan argumen bukan string
print("Hasil konversi 456 adalah:", konversi_angka(456))
