import json

with open('file.json') as data_student:

    data = json.load(data_student)

murid = data['student']

print(data)