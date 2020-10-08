# 1. Data structure
Data structure merupakan sebuah hal yang fundamental dalam pengembangan software. Data structure diperlukan untuk menyusun (organizing, managing, and storing) apa saja yang diperlukan di dalam program. Hal ini sangat diperlukan dalam membuat sebuah program karena membantu developer bekerja lebih efisien.

## 1.1 Data Structure pada Python
Secara built in, di dalam bahasa Python sudah terdapat data structure yang disebut List, Dictionary, Tuple, dan Set. Python juga memberikan aksesbilitas kepada developer untuk membuat data structure sendiri dengan menggunakan Function. 

### 1.1.1 Penjelasan setiap data structure pada Python
Data structure Python built in adalah List, Dictionary, Tuple, dan Set. 

### 1.1.1.1 List
Pengertian: List merupakan data structure yang digunakan untuk menyimpan kumpulan data dari tipe yang berbeda. Data yang ada di dalam list disebut dengan Index. Index terdapat dua jenis yaitu *positive index* yang berguna untuk mengakses index dengan urutan index pertama hingga akhir dan *negative index* yang berguna untuk mengakses dari urutan index terakhir ke urutan pertama. 
<br />
Contoh: <br/>
* catatan: index pertama dimulai dari angka 0, bukan 1<br />

a. Menampilkan semua index dari list <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`print(list_saya)` <br />
#hasil <br />
`[1, 2, 3, 5, 'empat', 6, 'tujuh', 'delapan']`

b. Menampilkan enam index dari list <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`print(list_saya[:5])` <br />
#hasil<br />
`[1, 2, 3, 5, 'empat']` <br />

c. Menampilkan index ke 5 dari list <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`print(list_saya[4])` <br />
#hasil <br />
`5` 

d. Menampilkan index dari index terakhir ke index awal <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`print(list_saya[-7])` <br />
#hasil <br />
`2` 


d. Contoh lebih banyak dapat dilihat di https://www.programiz.com/python-programming/list

### 1.1.1.2 Dictionary
Pengertian: Dictonary adalah data structure yang menyimpan data berupa pasangan `key-value`. <br />
Contoh: <br />

a. Dictionary sederhana <br />
`warna_dan_angka = {'warna': 'merah', 'angka': 1}`
`print (warna_dan_angka['warna'])`
`print (warna_dan_angka['angka'])`
#hasil <br />
`merah`
`1`

b. Contoh lebih banyak dapat dilihat di https://www.programiz.com/python-programming/dictionary

### 1.1.1.3 Tuple
Pengertian: 