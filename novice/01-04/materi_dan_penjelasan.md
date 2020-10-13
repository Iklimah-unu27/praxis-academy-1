# 1. UML 
UML atau Unified modeling language merupakan sebuah tool untuk mendesain atau menjelaskan sebuah project terhadap software yang akan dikembangkan.

UML selain berguna sebagai blueprint untuk sebuah program, juga berguna sebagai media untuk menjelaskan sebuah project terhadap seseorang yang terlibat di dalam project.

# 2. Advanced OOP
Dalam advanced OOP pada python tedapat 5 Jenis:

1. Multiple inheritance
2. Multilever inheritance
3. method resolution order (MRO)
4. Method overriding
5. Method types: static, dan class

## 2.1 Multiple inheritance 

Inheritance adalah sebuah cara untuk bisa menurunkan sebuah class ke class lainnya. Inheritance merupakan salah satu implementasi pada programming untuk menghindari DRY (don't repeat yourself) sehingga proses pengembangan software lebih efisien. 

Multiple inheritance adalah ketika sebuah class mendapatkan turunan dari lebih dari satu class dasar. Class yang mendapatkan turunan mendapatkan semua fitur dari dari class dasar. 

Contoh: 

`class DataPekerja():`<br />              
>`	def __init__(self, name, uid):`<br />  
>>`		self.name = name`<br />  
>>`		self.uid = uid`<br />  
  
`class Job():`<br />              
>`	def __init__(self, pay, role):`<br />  
>>`		self.pay = pay `<br />  
>>`		self.role = role`<br />  

`class TeamLeader(DataPekerja, Job):`<br />   
>`	def __init__(self, name, uid, pay, exp, role): #name, uid didapat dari class Team Member, pay di dapat dari class Worker dan, exp di dapat dari class Team Leader.`<br />
>>`		self.exp = exp`<br/>
>>`		DataPekerja.__init__(self, name, uid) #memanggil dan mengisi value`<br />
>>`		Job.__init__(self, pay, role)`<br />
>>`		print("Team leader bernama {}, dengan nomor UID {} memiliki gaji sebesar {} /bulan, dengan pengalaman {} sebagai {}.".format(self.name, self.uid,  self.pay, self.exp, self.role))`<br />

`TL = TeamLeader('Lorem Ipsum', '#1111', 'Rp 25,000,000', '5 tahun', 'programmer') #menambahkan value untuk class`

## 2.2 Multilevel inheritance

Apabila multiple inheritance adalah suatu class turunan (child Class) mendapatkan turunan dari dua class dasar (parent Class), multilever adalah apabila parent class menunrunkan class ke child class secara berurutan seperti ini: Base class (parent Class) > class turunan (child Class) > class turunan (grand child Class).

Contoh: 

`class Orang(): # Base Class`<br />
>`	def __init__(self, nama): `<br />
>>`		self.nama = nama` <br />
	 
`	def getName(self): #untuk mendapatkan nama`<br />
		`return self.nama` <br />
 

`class Usia(Orang): #Sub class`<br />
>`	def __init__(self, name, usia): `<br />
>>`		Orang.__init__(self, name) `<br />
>>`		self.usia = usia `<br />

>`	def getUsia(self): # Untuk mendapatkan usia`<br />
>>`		return self.usia `<br />


`class Lengkap(Usia): #Turunan dari subclass`<br />
>`	def __init__(self, nama, usia, alamat): `<br />
>>`		Usia.__init__(self, nama, usia) `<br />
>>`		self.alamat = alamat `<br />

>`	def getAlamat(self): #Untuk mendapatkan alamat`<br />
>>`		return self.alamat	` <br />

`Identitas = Lengkap("Lorem", 23, "Ipsum") #menambahkan value`<br />
`print('Orang bernama', Identitas.getName(), 'berusia', Identitas.getUsia(), 'saat ini tinggal di', Identitas.getAlamat()) #print semua data yang telah ditentukan` 








