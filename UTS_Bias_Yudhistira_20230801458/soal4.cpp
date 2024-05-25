#include <iostream>
using namespace std;

int main() {
    int tahun_lahir, usia;
    const int tahun_sekarang = 2024;

    cout << "Masukkan Tahun Lahir Kalian: ";
    cin >> tahun_lahir;

    usia = tahun_sekarang - tahun_lahir;

    cout << "Berarti Usia Kalian sekarang adalah " << usia << " Tahun" << endl;

    return 0;
}
