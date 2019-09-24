import csv

csvfile = open('data.csv')
vol_dosis = []
readCSV = csv.reader(csvfile,delimiter=';')
for row in readCSV:
   	vol_dosis.append(row[3])


print vol_dosis