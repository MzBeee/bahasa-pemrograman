# Sel 1: Import Modul
import sqlite3

# Sel 2: Membuat Koneksi dan Mengelola Database SQLite
def kelola_database_sqlite():
    # Membuat koneksi ke database SQLite
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Membuat tabel
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT,
                      age INTEGER)''')

    # Menambahkan data ke tabel
    cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Alice', 30))
    cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', ('Bob', 25))

    # Commit perubahan
    conn.commit()

    # Mengambil data dari tabel
    cursor.execute('''SELECT * FROM users''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Menutup koneksi
    conn.close()

# Sel 3: Menjalankan Fungsi
kelola_database_sqlite()
