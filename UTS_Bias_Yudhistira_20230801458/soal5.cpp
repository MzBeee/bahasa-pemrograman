#include <iostream>
using namespace std;

int main() {
    int angka_pertama, angka_kedua;

    // Meminta input dari pengguna
    cout << "Masukkan Angka Pertama : ";
    cin >> angka_pertama;
    cout << "Masukkan Angka Kedua   : ";
    cin >> angka_kedua;

    // Menghitung dan menampilkan hasil operasi aritmatika
    cout << "Penjumlahan            : " << angka_pertama + angka_kedua << endl;
    cout << "Pengurangan            : " << angka_pertama - angka_kedua << endl;
    cout << "Perkalian              : " << angka_pertama * angka_kedua << endl;
    cout << "Pembagian              : " << angka_pertama / angka_kedua << endl;

    return 0;
}
