# 15 Puzzle Solver

## Deksripsi Singkat
Program ini merupakan solver dari 15 puzzle memanfaatkan konsep Branch and Bound. Program ini dibuat sebagai Tugas Kecil 3 Stima Tahun Ajaran 2021/2022.

## Requirements (Windows)
Telah menginstall python 3 pada PC. Untuk instalasi python dapat dilihat pada https://realpython.com/installing-python/

Telah menginstall numpy. numpy dapat di-install menggunakan perintah berikut di commandprompt atau shell

```shell
pip install numpy
```

## Cara mengcompile dan menjalankan program
1. Download repo ini dalam bentuk zip melalui website github lalu ekstrak file zip tersebut

2. Buka folder src yang di dalamnya terdapat main.py

3. Jalankan cmd pada folder tersebut

4. Pada command prompt jalankan perintah "python main.py"

5. Program akan terbuka di command prompt

6. Program akan meminta masukkan angka 1 atau 2 sebagai pilihan cara input file (1 = random generated, 2 = input berupa nama file)

7. Apabila memilih pilihan 2, program akan meminta masukkan nama file (Contoh = "tes.txt"). Nama file yang diterima adalah file dalam bentuk txt yang sudah dimasukkan ke dalam folder test. File txt yang dianggap benar merupakan file text yang terdiri atas 16 angka (1-16) yang dibagi jadi 4 baris. Setiap baris mengandung 4 angka yang dipisahkan oleh spasi. Ubin yang kosong direpresentasikan dengan angka 16.
Contoh file txt yang memenuhi syarat adalah sebagai berikut
```shell
1 2 3 4
5 6 16 8
9 10 12 13
14 15 7 11
```

8. Program akan menampilkan hasil pencarian solusi dari puzzle

## Author
Rheza Rizqullah Ecaldy / 13520060

