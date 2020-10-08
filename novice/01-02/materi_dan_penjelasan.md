# 1. Data structure
Data structure merupakan sebuah hal yang fundamental dalam pengembangan software. Data structure diperlukan untuk menyusun (organizing, managing, and storing) apa saja yang diperlukan di dalam program. Hal ini sangat diperlukan dalam membuat sebuah program karena membantu developer bekerja lebih efisien.

## 1.1 Data Structure pada Python
Secara built in, di dalam bahasa Python sudah terdapat data structure yang disebut List, Dictionary, Tuple, dan Set. Python juga memberikan aksesbilitas kepada developer untuk membuat data structure sendiri yang disebut *user-defined Data Structure*

### 1.1.1 Built in Data Structure pada Python
Data structure Python built in adalah List, Dictionary, Tuple, dan Set. 

### 1.1.1.1 List
Pengertian: List merupakan data structure yang digunakan untuk menyimpan kumpulan data dari value yang berbeda. Data yang ada di dalam list disebut dengan Index. Index terdapat dua jenis yaitu *positive index* yang berguna untuk mengakses index dengan urutan index pertama hingga akhir dan *negative index* yang berguna untuk mengakses dari urutan index terakhir ke urutan pertama. 
<br />
Contoh: <br/>
* catatan: index pertama dimulai dari angka 0, bukan 1<br />

a. Menampilkan semua index dari list <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`print(list_saya)` <br />
output: <br />
`[1, 2, 3, 5, 'empat', 6, 'tujuh', 'delapan']`

b. Menampilkan enam index dari list <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`print(list_saya[:5])` <br />
output:<br />
`[1, 2, 3, 5, 'empat']` <br />

c. Menampilkan index ke 5 dari list <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`print(list_saya[4])` <br />
output: <br />
`5` 

d. Menampilkan index dari index terakhir ke index awal <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`print(list_saya[-7])` <br />
output: <br />
`2` 

d. Menambahkan index dalam list <br />
`list_saya = [1,2,3,5, 'empat', 6, 'tujuh', 'delapan']` <br />
`list_saya.append(100)` <br />
output: <br />
`[1, 2, 3, 5, 'empat', 6, 'tujuh', 'delapan', 100]` 

e. Contoh lebih banyak dapat dilihat di https://www.programiz.com/python-programming/list


### 1.1.1.2 Tuple
Pengertian: Tuple juga merupakan data structure yang berfungsi menyimpan data seperti list, namun di dalam Tuple, Index tidak dapat diubah sama sekali. 


### 1.1.1.3 Dictionary
Pengertian: Dictonary adalah data structure yang menyimpan data berupa pasangan `key-value`. <br />
Contoh: <br />

a. Dictionary sederhana <br />
`warna_dan_angka = {'warna': 'merah', 'angka': 1}`<br />
`print (warna_dan_angka['warna'])`<br />
`print (warna_dan_angka['angka'])`<br />
output: <br />
`merah`<br />
`1` <br />

b. Contoh lebih banyak dapat dilihat di https://www.programiz.com/python-programming/dictionary

### 1.1.1.4 Sets
Pengertian: Sets adalah kumpulan dari unordered value yang bersifat unik. Jadi, apabila di dalam sets terdapat beberapa value yang identik (duplikat), maka akan menghasilkan output nilai yang duplikat hanya satu kali.


Contoh: <br />
a. Output sets
`set_saya = {1, 2, 3, 4, 5, 5, 5}` <br />
`print(set_saya)` <br />
output:<br />
`{1, 2, 3, 4, 5}`<br />

b. Menambah value pada sets<br />
`set_saya = {1, 2, 3, 4, 5, 5, 5}` <br />
`set_saya.add(100)` <br />
`print(set_saya)`
output:<br />
`{1, 2, 3, 4, 5, 100}`<br />


# 2. Modules di Python


# 3. Input dan Output

Contoh: <br />
`nama = input('masukkan nama: ')`<br />
user input: `ini nama`<br />
`print (f'nama kamu adalah' {nama})`<br />
output: <br />
`nama kalu adalah ini nama` 


# 4. Errors and Exceptions

Contoh: <br />
a. Contoh Errors
`nama = input('masukkan nama:')`<br/>
`print f'nama kamu adalah {nama}'`<br />
output error <br />
`  File "/Users/macbookpro/Downloads/from_random_import_randint.py", line 2
    print f'nama kamu adalah {nama}'
                                   ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(f'nama kamu adalah {nama}')?` di line terakhir ini menunjukkan jenis error

b. Contoh Exceptions
`string_tidak_bisa_digabung_dengan_int = 'satu' + 1`<br />
`print (string_tidak_bisa_digabung_dengan_int)`<br />
output: exceptions <br />
`Traceback (most recent call last):
  File "/Users/macbookpro/Downloads/from_random_import_randint.py", line 1, in <module>
    string_tidak_bisa_digabung_dengan_int = 'satu' + 1
TypeError: can only concatenate str (not "int") to str` di line ini menunjukkan bahwa string tidak bisa digabung dengan int<br />

c. Contoh Handling Exceptions <br />
`while True:
    try:
        harus_angka = int(input("Masukan angka: ")) #di kode ini user diminta memasukkan angka
        break
    except ValueError:
        print("bukan angka, masukan angka") #apabila tidak memasukkan angka, maka hasil tersebut akan muncul sebagai fitur menghandle error dan memberikan user kesempatan untuk input data yang sesuai.` 












