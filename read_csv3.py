import csv

file = csv.reader(open('ServiceTag.csv', "rt"))

for row in file:
    print(row)
