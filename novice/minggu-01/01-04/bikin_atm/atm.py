balance=100000
pin_benar = 101010

print("Halo, selamat datang di bank yang uangnya banyak")

while True:
	try:
		pin = int(input("Silakan masukkan PIN: "))
		if pin == pin_benar:
			break
		print('PIN, salah masukkan kembali PIN')
	except Exception as sudah_benar:
		print()

print("1. Balance \n2. Withdraw \n3. Deposit \n4. Quit")

Option=int(input("Enter Option: "))


#option 1
if Option==1:
	print("Balance  Rp ",balance)

	print("Apakah ada kepeluan lagi?")
	print("1. Ya \n2. Tidak")
	Lanjut=int(input("Enter Option: "))

	if Lanjut==2:
		print('terima kasih sudah menggunakan layanan kami.')	

	if Lanjut==1:
		print("1. Withdraw \n2. Deposit \n3. Quit")	
		Option=int(input("Enter Option: "))

		if Option==1:
			print("Balance  Rp  ",balance)
			Withdraw=float(input("Masukkan jumlah Rp "))
			if Withdraw>0:
				saldo_sisa=(balance-Withdraw)
				print("Foreward Balance  Rp ",saldo_sisa, ". Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")
			elif Withdraw>balance:
				print("Saldo tidak cukup. Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")
			else:
				print("Tidak ada transaksi dilakukan. Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")

		if Option==2:
			print("Balance  Rp ",balance)
			Deposit=float(input("Enter deposit amount Rp "))
			if Deposit>0:
				forewardbalance=(balance+Deposit)
				print("Forewardbalance  Rp ",forewardbalance, ". Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")
			else:
				print("Tidak ada transaksi dilakukan. Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")

		if Option==3:
			exit("Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")
		
		exit()


# #option 2
if Option==2:
	print("Balance  Rp  ",balance)
	Withdraw=float(input("Masukkan jumlah Rp "))
	if Withdraw>0:
		sisa_uang=(balance-Withdraw)
		print("Foreward Balance  Rp ",sisa_uang, )
	elif Withdraw>balance:
		print("Saldo tidak cukup.")
	else:
		print("Tidak ada transaksi dilakukan.")

	print("Apakah ada kepeluan lagi?")
	print("1. Ya \n2. Tidak")
	Lanjut=int(input("Enter Option: "))

	if Lanjut==2:
		print('terima kasih sudah menggunakan layanan kami.')	

	if Lanjut==1:
		print("1. Balance \n2. Deposit \n3. Quit")	
		Option=int(input("Enter Option: "))

		if Option==1:
			print("Balance  Rp ",sisa_uang, ". Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")

		if Option==2:
			print("Balance  Rp ",sisa_uang)
			Deposit=float(input("Enter deposit amount Rp "))
			if Deposit>0:
				forewardbalance=(sisa_uang+Deposit)
				print("Forewardbalance  Rp ",forewardbalance)
			else:
				print("None deposit made")

		if Option==3:
			exit("Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")
		
		exit()			


# #ption 3
if Option==3:
	print("Balance  Rp ",balance)
	Deposit=float(input("Enter deposit amount Rp "))
	if Deposit>0:
		forewardbalance=(balance+Deposit)
		print("Forewardbalance  Rp ",forewardbalance)
	else:
		print("None deposit made")


	print("Apakah ada kepeluan lagi?")
	print("1. Ya \n2. Tidak")
	Lanjut=int(input("Enter Option: "))

	if Lanjut==2:
		print('terima kasih sudah menggunakan layanan kami.')	

	if Lanjut==1:
		print("1. Balance \n2. Withdraw \n3. Quit")	
		Option=int(input("Enter Option: "))

		if Option==1:
			print("Balance  Rp ",forewardbalance, ". Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")

	if Option==2:
		print("Balance  Rp  ",forewardbalance)
		Withdraw=float(input("Masukkan jumlah Rp "))
		if Withdraw>0:
			sisa_uang=(forewardbalance-Withdraw)
			print("Sisa uang  Rp ",sisa_uang, "Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")
		elif Withdraw>forewardbalance:
			print("Saldo tidak cukup.")
		else:
			print("Tidak ada transaksi dilakukan.")

		if Option==3:
			exit("Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")
		
		exit()

if Option==4:
	exit("Terima kasih sudah menggunakan layanan kami, tunggu kartu keluar.")
