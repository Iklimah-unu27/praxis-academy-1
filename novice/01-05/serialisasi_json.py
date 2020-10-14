import json

with open('/Users/macbookpro/Google Drive/Programming/bootcamp_python_2020/praxis-academy/novice/01-05/file.json') as hewan_data:
    hewan = json.load(hewan_data)

nama_hewan = hewan['hewan']
#jumlah_kaki = hewan['jumlah_kaki']

print(hewan)