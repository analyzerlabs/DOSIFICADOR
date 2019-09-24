import csv

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    usrid = []
    price = []
    product = []
    for row in readCSV:
        usrid.append(row[0])
        price.append(row[1])
        product.append(row[2])

    print usrid