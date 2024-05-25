#include <iostream>
#include <string>

using namespace std;

// Struct TanggalLahir
struct TanggalLahir {
    int tanggal;
    int bulan;
    int tahun;
};

// Struct Alamat
struct Alamat {
    string namaJalan;
    int nomorRumah;
    string kota;
    string provinsi;
};

// Struct Mahasiswa (Mhs)
struct Mhs {
    int nim;
    string nama;
    Alamat alamat;
    string tempat;
    TanggalLahir tanggalLahir;
};

int main() {
    // Array of struct Mahasiswa untuk menyimpan data 5 mahasiswa
    Mhs mahasiswa[5];

    // Input data untuk 5 mahasiswa
    for (int i = 0; i < 5; ++i) {
        cout << "Masukkan data untuk mahasiswa ke-" << i + 1 << endl;
        cout << "NIM: ";
        cin >> mahasiswa[i].nim;
        cout << "Nama: ";
        cin.ignore(); // Membersihkan buffer agar getline() berfungsi dengan baik
        getline(cin, mahasiswa[i].nama);
        cout << "Alamat:" << endl;
        cout << "Nama Jalan: ";
        getline(cin, mahasiswa[i].alamat.namaJalan);
        cout << "Nomor Rumah: ";
        cin >> mahasiswa[i].alamat.nomorRumah;
        cout << "Kota: ";
        cin.ignore();
        getline(cin, mahasiswa[i].alamat.kota);
        cout << "Provinsi: ";
        getline(cin, mahasiswa[i].alamat.provinsi);
        cout << "Tempat Lahir: ";
        getline(cin, mahasiswa[i].tempat);
        cout << "Tanggal Lahir (DD MM YYYY): ";
        cin >> mahasiswa[i].tanggalLahir.tanggal >> mahasiswa[i].tanggalLahir.bulan >> mahasiswa[i].tanggalLahir.tahun;
    }

    // Menampilkan data mahasiswa yang telah diinput
    cout << "\nData Mahasiswa:" << endl;
    for (int i = 0; i < 5; ++i) {
        cout << "Mahasiswa ke-" << i + 1 << ":" << endl;
        cout << "NIM: " << mahasiswa[i].nim << endl;
        cout << "Nama: " << mahasiswa[i].nama << endl;
        cout << "Alamat: " << mahasiswa[i].alamat.namaJalan << " No. " << mahasiswa[i].alamat.nomorRumah << ", " << mahasiswa[i].alamat.kota << ", " << mahasiswa[i].alamat.provinsi << endl;
        cout << "Tempat Lahir: " << mahasiswa[i].tempat << endl;
        cout << "Tanggal Lahir: " << mahasiswa[i].tanggalLahir.tanggal << "/" << mahasiswa[i].tanggalLahir.bulan << "/" << mahasiswa[i].tanggalLahir.tahun << endl;
        cout << endl;
    }

    return 0;
}