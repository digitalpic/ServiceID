import csv
import sys


if len(sys.argv) < 3:
    print("++++++++ SERVICE TAG FINDER ++++++++")
    print("Please enter the name of the person.")
    print("++++++++++++++++++++++++++++++++++++")
    search_1 = input("Search for:")
else:
    search_1 = sys.argv[1]


csvfile = open('ServiceTag.csv', 'rt', encoding="Latin-1")
csvfile.seek
reader = csv.reader(csvfile, dialect='excel', delimiter=",", quotechar="'")

for row in reader:
    if any(search_1 in col for col in row):
        print("Results = " + ' '.join(row))
        break

else:
    print("No results found for " + search_1)
