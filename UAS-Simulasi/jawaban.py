import datetime
import json
import statistics

class Perawatan:
    def __init__(self, pasien, dokter, jenis_perawatan, hasil_perawatan, tanggal_perawatan=None):
        self.pasien = pasien
        self.dokter = dokter
        self.jenis_perawatan = jenis_perawatan
        self.hasil_perawatan = hasil_perawatan
        self.tanggal_perawatan = tanggal_perawatan if tanggal_perawatan else datetime.datetime.now()

data_perawatan = []

def tambah_perawatan():
    pasien = input("Masukkan nama pasien: ")
    dokter = input("Masukkan nama dokter: ")
    jenis_perawatan = input("Masukkan jenis perawatan: ")
    hasil_perawatan = float(input("Masukkan hasil perawatan (nilai numerik): "))
    tanggal_input = input("Masukkan tanggal perawatan (YYYY-MM-DD) atau tekan Enter untuk tanggal saat ini: ")

    if tanggal_input:
        try:
            tanggal_perawatan = datetime.datetime.strptime(tanggal_input, "%Y-%m-%d")
        except ValueError:
            print("Format tanggal tidak valid. Menggunakan tanggal saat ini.")
            tanggal_perawatan = datetime.datetime.now()
    else:
        tanggal_perawatan = datetime.datetime.now()

    perawatan = Perawatan(pasien, dokter, jenis_perawatan, hasil_perawatan, tanggal_perawatan)
    data_perawatan.append(perawatan)
    print(f"Data perawatan untuk pasien {pasien} telah ditambahkan.")

def simpan_data(filename='data_perawatan.json'):
    with open(filename, 'w') as file:
        json_data = [perawatan.__dict__ for perawatan in data_perawatan]
        json.dump(json_data, file, default=str)
    print(f"Data perawatan telah disimpan ke {filename}.")

def analisis_data():
    if not data_perawatan:
        print("Tidak ada data perawatan untuk dianalisis.")
        return

    hasil_perawatan = [p.hasil_perawatan for p in data_perawatan]
    mean_hasil = statistics.mean(hasil_perawatan)
    median_hasil = statistics.median(hasil_perawatan)

    print("Analisis Data Perawatan:")
    print(f"Rata-rata hasil perawatan: {mean_hasil}")
    print(f"Median hasil perawatan: {median_hasil}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah data perawatan")
        print("2. Simpan data ke file")
        print("3. Analisis data perawatan")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            tambah_perawatan()
        elif pilihan == '2':
            simpan_data()
        elif pilihan == '3':
            analisis_data()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()