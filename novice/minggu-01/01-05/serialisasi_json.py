import json

with open('/Users/macbookpro/Google Drive/Programming/bootcamp_python_2020/praxis-academy/novice/01-05/file.json') as data_student:
    data = json.load(data_student)

murid = data['student']

print(data)