import csv

with open('adblock.csv','r') as first_file:
    csv_reader1 = csv.reader(first_file)
    for line in csv_reader1:
        print(line)



with open('client_reuest.csv', 'r') as second_file:
    csv_reader2 = csv.reader(second_file)
    for line in csv_reader2:
        print(line)