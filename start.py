from pip._vendor import requests
import json

url = 'https://raw.githubusercontent.com/bhargav-velisetti/flink_examples/master/data/cruise_ship_schema.json'

response = requests.get(url)
print(response)
if response.status_code == 200:
    data = response.json()
    print(data)
    crew_value = data.get('crew')
    if crew_value is not None:
        print("Value for key 'crew':", crew_value)
    else:
        print("Key 'crew' not found in the JSON data.")

    #2ND: 2. Read this json file, loop over it and print values for the key = firstName https://github.com/bhargav-velisetti/apache_beam_examples_java/blob/master/data/sample-data.json
    for item in data:
        if 'firstName' in item:
            print("First Name:", item['firstName'])
        else:
            print("Key 'firstName' not found in this item.")
else:
    print("Failed to fetch data from the URL.")


#3 TO 8
list_a=[0,1,2,3,4,5,6]

print('the fifth element is:'+ str(list_a[4]))
print('Last 3 elements', list_a[-3:])
print("Length of the list:", len(list_a))

dict_a = {'a': 1, 'b': 2}
print("Keys of dict_a:", list(dict_a.keys()))
print("Values of dict_a:", list(dict_a.values()))

if 'b' in dict_a:
    print("Value of key 'b':", dict_a['b'])
else:
    print('b is not a key in dictionary')


