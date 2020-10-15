## Functional Programming
Function merupakan sebuah blok dari kode yang didesain untuk melakukan sebuah proses secara spesifik. Jadi, ketika akan melakukan sebuah proses data yang akan defined menggunakan function, maka hanya diperlukan untuk 'memanggil' function yang diperlukan.

Apabila seorang developer perlu membuat program yang memiliki fitur yang mengerjakan pekerjaan untuk beberapa kali, maka developer tidak perlu untuk membuat kode yang diperlukan untuk memproses sebanyak pekerjaan yang perlu dikerjaan tersebut. Hal ini karena dengan menggunakan function, developer hanya perlu menulis satu function untuk bisa memproses beberapa pekerjaan yang diperlukan. Intinya adalah, dengan menggunakan function berarti menghindari DRY (don't repeat yourself).

### Define sebuah function
Untuk membuat sebuah function, berikut ini adalah cara untuk membuatnya:
1. Bagian function dimulai dengan def diikuti dengan nama function dan parentheses ().

2. Parameter atau argument yang ditulis di dalam parentheses. 

3. Statement return menjelaskan kalau sebuah function berhenti di sana. 

#### Syntax
`def functionname(parameters):`
>`   return [expression]`

#### Contoh
`def favorite_os(nama_os):` 

>`    return 'OS favorit saya adalah {}'.format(nama_os.title())`

`print(favorite_os('linux'))`

