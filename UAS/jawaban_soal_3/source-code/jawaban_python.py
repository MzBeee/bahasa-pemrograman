# Import Modul
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk Menangani Klik Tombol
def tombol_ditekan():
    messagebox.showinfo("Informasi", "Tombol telah ditekan!")

# Membuat Jendela GUI
def buat_aplikasi():
    # Membuat jendela utama
    jendela = tk.Tk()
    jendela.title("Contoh GUI dengan Tkinter")
    
    # Menambahkan label
    label = tk.Label(jendela, text="Selamat datang di aplikasi GUI!")
    label.pack(pady=10)
    
    # Menambahkan tombol
    tombol = tk.Button(jendela, text="Tekan Saya", command=tombol_ditekan)
    tombol.pack(pady=10)
    
    # Menjalankan aplikasi
    jendela.mainloop()

# Menjalankan Aplikasi
buat_aplikasi()
