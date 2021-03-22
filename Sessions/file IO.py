import os
base_path=os.path.dirname(os.path.dirname(__file__))
print(base_path)

asset_path=os.path.join(base_path,'assets')

if not os.path.exists(asset_path):
    os.makedirs(asset_path)

text_file_path=os.path.join(asset_path,'text.txt')

# _file = open(text_file_path, 'w')
# _file.write('This is my first line\n')
# _file.write('This is my second line.\n')
# _file.close()

# with open(text_file_path, 'w') as _file:
#     _file.write('This is my first line\n')
#     _file.write('This is my second line.\n')
#
# if os.path.exists(text_file_path):
#     with open(text_file_path, 'r') as _file:
#          for i in _file.readlines():
#              print(i, end="")

_data = {
    123: {
        'name': 'pavan',
        'addresss': {
            'line1': 'address line 1',
            'line2': 'address line 2',
            'line3': 'address line 3',
            'city': 'Pune'
        },
        'contact': '12345688422',
        'email': 'pavan@pavan.com'
    },
    124: {
        'name': 'Jimmy',
        'addresss': {
            'line1': 'address line 1',
            'line2': 'address line 2',
            'line3': 'address line 3',
            'city': 'Pune'
        },
        'contact': '12345688422',
        'email': 'jimmy@jimmy.com'
    }
}

import json
JSON_FILE_PATH = os.path.join(asset_path, 'my_json.json')

with open(JSON_FILE_PATH, 'w') as _file:
    json.dump(obj=_data, fp=_file)

with open(JSON_FILE_PATH, 'r') as _file:
    json_data = json.load(_file)

    print(json_data.get('123'))

# _data = [
#     ['no', 'name', 'age', 'contact'],
#     [1, 'Pavan  Maradia', 31, 9840548303],
#     [2, 'Jimmy', 33, 9343923893],
#     [3, 'Kirti', '-', 94345443434],
#     [4, 'Seema', '-', 93345443434],
#     [5, 'Vaibhavi', '-', 94346743434]
# ]
#
# import csv
# CSV_FILE = os.path.join(asset_path, 'my_csv.csv')
# with open(CSV_FILE, 'w') as _file:
#     csv_writer = csv.writer(_file)
#     csv_writer.writerows(_data)
#
# with open(CSV_FILE, 'r') as _file:
#     csv_read = csv.reader(_file)
#     for i in csv_read:
#         print(i)