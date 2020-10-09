
def createDict(filename=''):
    import csv
    file =[]
    with open(filename, 'r') as second_file:
        csv_reader2 = csv.DictReader(second_file,delimiter=';')
        for line in csv_reader2:
            file.append(line)
    return file


first_file = createDict('client_reuest.csv')
second_file = createDict('adblock.csv')

print(first_file)
print(second_file)

first_file.sort(key=lambda add: int(add['Budget']) / int(add['Duration']))
print(first_file)