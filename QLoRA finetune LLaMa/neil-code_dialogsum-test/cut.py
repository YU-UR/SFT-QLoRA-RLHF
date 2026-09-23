import csv
import json


def crop_json(file_path, num_lines, new_file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    cropped_data = data[:num_lines]

    with open(new_file_path, 'w') as new_file:
        json.dump(cropped_data, new_file)


# file_paths = [
#     {'input': './data/corpus/train.json', 'size': 2000, 'output': './data/corpus-cut/train.json'},
#     {'input': './data/corpus/test.json', 'size': 500, 'output': './data/corpus-cut/test.json'},
#     {'input': './data/corpus/val.json', 'size': 500, 'output': './data/corpus-cut/val.json'}
# ]

#
# for file_path in file_paths:
#     crop_json(file_path['input'], file_path['size'], file_path['output'])


def crop_csv(file_path, num_lines, new_file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    cropped_data = data[:num_lines]

    with open(new_file_path, 'w') as new_file:
        writer = csv.writer(new_file)
        writer.writerows(cropped_data)


file_paths = [
    {'input': './train.csv', 'size': 2000, 'output': './train.csv'},
    {'input': './test.csv', 'size': 500, 'output': './test.csv'},
    {'input': './validation.csv', 'size': 500, 'output': './validation.csv'}
]

for file_path in file_paths:
    crop_csv(file_path['input'], file_path['size'], file_path['output'])
