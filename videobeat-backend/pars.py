

def mainflow():

    def createDict(filename=''):
        """Create a dictionary out of a csv file
        if other delimiter than ";" in
        csv is used. It has to be specified in line 14 

        argument: a csv filename with ';' delimiter - string """
        import csv
        file =[]
        with open(filename, 'r') as second_file:
            csv_reader2 = csv.DictReader(second_file,delimiter=';')
            for line in csv_reader2:
                file.append(line)
        return file


    
    #Creating and sorting lists of dictionaries
    first_file = createDict('client_request.csv')
    second_file = createDict('adblock.csv')
    # sorting client request by values Descending
    first_file.sort(
        key=lambda add: int(add['Budget']) / int(add['Duration']),
        reverse=True),


    # Count the whole ammount of time in client requests and adds
    # throw out the least profittable
    adds_time = 0
    adblock_time = 0
    for i in first_file:
        adds_time += int(i['Duration'])
    for i in second_file:
         adblock_time += int(i['Duratation'])
    while adds_time > adblock_time:
        adds_time = 0
        adblock_time = 0
        for i in first_file:
            adds_time += int(i['Duration'])
        for i in second_file:
            adblock_time += int(i['Duratation'])
        first_file.pop()

    print(adds_time)
    print(adblock_time)

    response ={"requests" : first_file,
            "adblocks": second_file}
    return response

mainflow()