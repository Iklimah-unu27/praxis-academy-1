### Object Serialisasi
Proses serialisasi merupakan cara untuk mengubah suatu struktur data menjadi bentuk linier yang dapat disimpan atau ditransmisikan melalui jaringan.

Di Python, serialisasi memungkinkan untuk mengambil data objek dan mengubahnya menjadi aliran byte yang dapat disimpan ke media penyimpanan atau dikirim melalui jaringan. Proses ini juga disebut sebagai marshalling. Sedangkan proses sebaliknya adalah mengambil aliran byte dan mengubahnya kembali menjadi struktur data dan proses tersebut disebut dengan deserialisasi atau unmarshalling

Python memberikan tiga pilihan modules di dalam standard librarynya yang memudahkan proses serialisasi dan deserialisasi, yaitu marshall, json, dan pickle. Sebagai tambahan Python juga mampu menggunakan xml untuk penggunaan serialisasi dan deserialisasi sebuah object.

Dari tiga module tersebut, marshall merupakan module tertua. Marshall tetap ada karena berguna untuk memproses read dan write bytecode yang telah dicompile oleh module Python atau oleh .pyc file yang didapat ketika interpreter mengimport sebuah module python. 

Sedangkan JSON adalah module paling baru diantara ketiga module tersebut. JSON merupakan module yang memungkinkan untuk bekerja dengan file JSON. JSON saat ini sangat direkomendasikan untuk digunakan karena human readable dan language independet, dan juga lebih ringan dibanding xml.
Dengan menggunakan JSON modul, developer bisa melakukan serialisasi dan deserialisasi untuk file bool, dict, int, float, list, string, tuple, dan None.

## Manual Pickle

Pickle module merupakan cara lain untuk melakukan serialisasi dan deserialisasi object pada Python. Hal ini berbeda dari json module karena pickle menserialisasikan object dalam sebuah format binary, yang artinya hasilnya itu tidak human readable. Meskipun begitu, proses serialisasi dan deserialisasi menggunakan pickle juga termasuk memiliki kemampuat yang cepat memproses dan dapat bekerja dengan banyak tipe Python termasuk object dengan custom defined.



