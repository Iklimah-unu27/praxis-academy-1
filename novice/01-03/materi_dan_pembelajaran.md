## OOP: 
Object oriented programming adalah salah satu paradigma dalam bahasa pemrograman. 

Agar sebuah program bisa berjalan menggunakan paradigma OOP, maka di dalam program tersebut biasanya terdapat sebuah class. Di dalam class terdapat attribut dan method.

Sebagai contoh, sebuah class berisi tentang binatang, di dalam class binatang terdapat binatang yang kita sebut sebagai attribut dan yang menyajikan informasi berupa mereka mengeluarkan suara atau cara bergerak dari setiap binatang disebut sebagai method. 

Jadi, di dalam class tersebut terdapat object dari binatang yang berisi binatang dan bagaimana binatang tersebut melakukan sesuatu.  

## CRC Card: 
Class-responsibility-collaboration atau disingkat menjadi CRC cards adalah alat yang digunakan untuk mendesign software object oriented. Awalnya CRC ditujukan sebagai alat untuk mengajar. CRC cards biasanya dibuat dari index cards yang terdiri dari:
1. Bagian atas kartu disebut sebagai class
2. Bagian kiri (di bawah class) sebagai responsibilities dari class. 
3. Bagian kanan disebut sebagai collaborator yang merupakan class lain yang akan berhubungan dengan responsibilities

## OOP pada Python:
Pengertian pada OOP secara umum sendiri sudah terdapat pada bagian tentang OOP di atas. 
Untuk OOP pada Python, sebuah object merupakan pusat dari hanya menampilkan data namun sebagai struktur dari program.
Object pada Python terdiri dari Class, attribut, dan method.

### Class 
Class merupakan sebuah kesatuan dari data dan function. Membuat sebuah class berarti membuat satu buah tipe object yang memberikan adanya instances dari tipe object yang akan dibuat.

Class digunakan untuk membuat struktur data yang ditentukan oleh pengguna. Function pada class disebut dengan methods, yang mengidentifikasi perilaku dan tindakan yang dapat dilakukan  oleh objek yang dibuat dari class dengan datanya.

Sebuah class merupakan sebuah blueprint untuk menunjukkan bagaimana sesuatu dapat didefinisikan namun belum memiliki data sama sekali.

Sementara class merupakan blueprint, sebuah instance adalah sebuah object yang terbuat dari sebuah class dan berisi data yang sebenarnya.

Singkatnya, apabila dianalogikan class adalah sebuah form atau questionnaire. Dan apabila class diisi data, maka akan seperti form atau questionnaire yang telah diisi, dan disebut sebagai instances. 

#### Contoh instantiate object Python: 

`>>> class Form:`
`...     pass`

Dengan syntax tersebut dapat membuat class Form tanpa attributers ataupun methods

### Membuat object baru dari class disebut dengan instantiating sebuah object.

Untuk meng-instantiate object Form baru, bisa menggunakan syntax berikut:

`>>> Form()`

Maka akan mendapatkan object pada `0x10341b518` seperti di bawah. Angka tersebut merupakan memory address yang menunjukkan di mana object Form disimpan pada komputer.

`<__main__.Form object at 0x10341b518>`


#### Class and Instance Attributes:

Contoh ini adalah membuat object dari class Form yang isi datanya akan berupa nama, usia, dan gender

`>>> class Form:
...     def __init__(self, nama, usia, gender):
...             self.nama = nama
...             self.usia = usia
...             self.gender = gender`

Kemudian apabila mengetik syntax seperti di bawah, maka akan muncul error karena belum terdapat value

`>>> Form()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() missing 3 required positional arguments: 'nama', 'usia', and 'gender'`

Untuk mengatasi hal tersebut, maka caranya adalah memberikan value untuk  'nama', 'usia', dan 'gender’. 

`>>> dimas = Form('dimas', 99, 'laki-laki')`
`>>> utami = Form('utami', 100, 'perempuan')`
 
Setelah membuat Form instances, maka kita dapat mengakses instance menggunakan dot notation:

`>>> dimas.usia
99
>>> utami.gender
'perempuan'`
