#Reading a CSV file using python3


# importing csv module
import csv

# reading csv file
with open('sample.csv', 'r') as csv_file:
    # creating a csv reader object
    read_csv = csv.reader(csv_file)

    # extracting field names through first row
    fields = next(read_csv)
    print(f'Column names are: {", ".join(fields)}')
    # extracting each row one by one
    for row in read_csv:
        print(f'Row details: {", ".join(row)}')