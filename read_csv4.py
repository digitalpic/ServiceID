import csv
import sys

start_again = True


def start():
    if len(sys.argv) < 2:
        print("                                     ")
        print("-+-+-+-+++++    SERVICE TAG FINDER     +++++-+-+-+-+")
        print(" Enter the first name of the person you are searching for.")
        print(" Press 'Enter' to view list. Press 'Ctrl + 'C' to exit.")
        search_1 = input(" Search for:")
    else:
        search_1 = sys.argv[1]

    csvfile = open('ServiceTag.csv', 'rt', encoding="Latin-1")
    csvfile.seek
    reader = csv.reader(csvfile, dialect='excel', delimiter=",")

    for row in reader:
        if any(search_1 in col for col in row):
            print("Results = " + ' - '.join(row))
    # TODO: Problem with returning print statement below even when results are
    # found.
    else:
        print("Results not found for: " + "'" + search_1 + "'")


while start_again:
    start()
