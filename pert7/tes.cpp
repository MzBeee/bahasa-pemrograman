@startuml essay.cpp

title Program Aritmetika Dasar

start

:Menampilkan Menu;
:1. Perkalian;
:2. Pembagian;
:3. Penjumlahan;
:4. Pengurangan;
:5. Keluar;
:Meminta input pilihan dari pengguna;

if (pilihan == 5) then (yes)
    :Menampilkan pesan "Terima kasih!";
    stop
else (no)
    if (pilihan >= 1 && pilihan <= 4) then (yes)
        :Meminta input angka pertama;
        :Meminta input angka kedua;

        if (pilihan == 1) then (Perkalian)
            :Hasil = angka1 * angka2;
            :Menampilkan hasil perkalian;
        elseif (pilihan == 2) then (Pembagian)
            if (angka2 == 0) then (ya)
                :Menampilkan pesan "Error: Pembagian dengan nol";
            else (tidak)
                :Hasil = angka1 / angka2;
                :Menampilkan hasil pembagian;
            endif
        elseif (pilihan == 3) then (Penjumlahan)
            :Hasil = angka1 + angka2;
            :Menampilkan hasil penjumlahan;
        elseif (pilihan == 4) then (Pengurangan)
            :Hasil = angka1 - angka2;
            :Menampilkan hasil pengurangan;
        endif
    else (tidak)
        :Menampilkan pesan "Pilihan tidak valid!";
    endif
    :Kembali ke menu;
endif

stop

@enduml
