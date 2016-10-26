import csv

f = open('ServiceTag.csv')
for row in csv.reader(f):
        # Insert search terms from the column needed.
    if row[1] == "admin":
        print(row)
        break

else:
    # TODO: Need to output only one line as shown.
    print(" Item not listed.")
