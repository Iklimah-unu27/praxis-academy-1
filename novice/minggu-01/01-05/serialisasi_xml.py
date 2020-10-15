from bs4 import BeautifulSoup

with open('/Users/macbookpro/Google Drive/Programming/bootcamp_python_2020/praxis-academy/novice/01-05/file.xml', 'r') as data_student:
	data = data_student.read()

student = BeautifulSoup(data, 'xml')
print(student)  