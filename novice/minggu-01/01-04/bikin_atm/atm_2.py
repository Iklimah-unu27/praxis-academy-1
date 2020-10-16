# import json
# with open('/Users/macbookpro/google drive/programming/bootcamp_python_2020/praxis-academy/novice/minggu-01/01-04/bikin_atm/data.json') as account:
#     accountfiledata = json.load(account)

class bank_account(object):
	def __init__(self, pin, balance):                 
		self.pin = pin
		self.balance = balance

	def VerifikasiUser(self, pin): #Verifikasi user
		try:
			if pin != self.pin:
				raise ValueError
			print("Pilih menu:")
		except ValueError:
			print("PIN Salah")
			exit(0)

	def __str__(self):
		return "Saldo anda adalah {}".format(self.balance)

	def checkbalance(self):
		return 'Rp' + str(self.balance) #self.balance untuk cek saldo

	def deposit(self, amount):
		self.balance += amount        

	def withdraw(self, amount):
		try:                          
			if self.balance >= amount: #saldo harus lebih besar atau sama dengan dari jumlah yang akan ditransfer
				self.balance -= amount #untuk mengurangi self.balance
			else:
				raise ValueError
		except ValueError:
				print("Saldo anda tidak cukup.")

	def filedata(self):              #function untuk menulis di file nasabah.
		return "{},{}".format(self.pin, self.balance)


#---------------------------

accountfile = open("nasabah.txt", "r+") #"r+" digunakan untuk membaca dan menulis file txt
accountfiledata = accountfile.read().split(",") #accountfile data ambil txt file dari accountfile
bank_user = bank_account(accountfiledata[0], float(accountfiledata[1])) #data untuk bank_user diambil dari accountfiledata di atas
pin = input("Masukan PIN:") 
bank_user.VerifikasiUser(pin) #menjalankan fitur verifikasiuser

while True: 
	answer=input("1.Deposit\n2.Tarik Tunai\n3.Cek Saldo\n4.Keluar\nPilih nomor menu untuk melanjutkan transaksi: ")
	if answer == "1":
		deposit_act= input("Masukan jumlah deposit:")
		bank_user.deposit(float(deposit_act))   #menggunakan function deposit
		print ("Jumlah saldo saat ini: " + bank_user.checkbalance())
	elif answer == "2":
		withdraw_act= input("Masukan jumlah uang yang akan ditarik ")
		bank_user.withdraw(float(withdraw_act))  #menggunakan function withdraw
	elif answer == "3":
		print( "Saldo anda adalah " + bank_user.checkbalance())  #menggunakan function balance
	elif answer == "4":
		print ("Terima kasih telah menggunakan ATM kami!")
		accountfile.close()
		exit(0) #untuk keluar dari ATM
	else:
		print ("Masukkan pilihan yang benar.")

	accountfile.seek(0) #untuk menghandle file data txt ketika program selesai dijalankan               
	accountfile.truncate(1) #untuk menampilkan hanya data terakhir yang diubah            
	accountfile.write(bank_user.filedata()) #untuk menjalankan function filedata