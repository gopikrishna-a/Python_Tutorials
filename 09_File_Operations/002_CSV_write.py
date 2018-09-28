#Writing a list into CSV file using python3


# importing csv module
import csv

#New list to add
new_line = ['Rob', '28', 'rob@hotmail.com']
# opn file in appending mode
with open('sample.csv', 'a') as csv_file:
    # creating a csv writer object
    write_csv = csv.writer(csv_file, dialect='excel')
    # Appending the newlist to csv file
    write_csv.writerow(new_line)