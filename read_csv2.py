import csv

username = []
servicetag = []
# open file
with open('ServiceTag.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    # read row by row
    rowNo = 0
    for row in reader:
        if rowNo >= 1:
            username.append(row[1])
            servicetag.append(row[3])

        rowNo = rowNo + 1

print(username)
print(servicetag)

# add the ability to query name
# whatName = input('Please enter the name of the person:' )
# queryName = usernames.index(whatName)
# returnServiceTag = servicetags[queryName]
# print(whatName, 'has laptop with', returnServiceTag)
