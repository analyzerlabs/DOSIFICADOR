import csv

with open('./data.csv', 'r') as _filehandler:
    csv_file_reader = csv.DictReader(_filehandler,delimiter=';',quotechar='|')

    for row in csv_file_reader:
        # Do something here
        print(row['id'])
        print(row['ubicacion'])