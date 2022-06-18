from csv import DictReader
import json

#Convert the csv file into dictionary

with open('world_price_indices', 'r') as data:
    #pass the file object to DictReader() to get the DictReader object
    reader = DictReader(data)
    # get a list of dictionaries from the reader
    list_of_data = list(reader)

    with open('world_indice.txt', 'w') as world_index_json:
        world_index_json.write(json.dumps(list_of_data))

    #print(list_of_data)

print(list_of_data[1]['names'])