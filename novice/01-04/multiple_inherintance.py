# Parent class 1
class DataPekerja():                   
	def __init__(self, name, uid): 
		self.name = name 
		self.uid = uid 
  
# Parent class 2
class Job():                 
	def __init__(self, pay, role): 
		self.pay = pay 
		self.role = role	

#Class team leader mendapat turunan dari dua parent class, di kasus ini karena team leader merupakan team member dan worker dan akan menampilkan gaji dan experince
class TeamLeader(DataPekerja, Job):         
	def __init__(self, name, uid, pay, exp, role): #name, uid didapat dari class Team Member, pay di dapat dari class Worker dan, exp di dapat dari class Team Leader.
		self.exp = exp 
		DataPekerja.__init__(self, name, uid) #memanggil dan mengisi value
		Job.__init__(self, pay, role)
		print("Team leader bernama {}, dengan nomor UID {} memiliki gaji sebesar {} /bulan, dengan pengalaman {} sebagai {}.".format(self.name, self.uid,  self.pay, self.exp, self.role))
		
TL = TeamLeader('Lorem Ipsum', '#1111', 'Rp 25,000,000', '5 tahun', 'programmer') #menambahkan value untuk class