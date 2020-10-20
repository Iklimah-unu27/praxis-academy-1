from bs4 import BeautifulSoup

with open('file.xml', 'r') as data_student:
	data = data_student.read()

student = BeautifulSoup(data, 'xml')
print(student)