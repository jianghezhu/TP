import json
import csv
data = [[2, 3], [3, 2], [1.0, -5.3]]

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('data.json', 'r') as json_file:
    data = json.load(json_file)

with open('complex_numbers.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['reel', 'imaginaire'])

    for complex_number in data:
        csv_writer.writerow(complex_number)