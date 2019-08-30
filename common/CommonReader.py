import csv

# Returns a csv reader
def commonCsvReader(csv_path):
    with open(csv_path, newline='') as csv_file:
        return csv.reader(csv_file, delimiter=',')
      