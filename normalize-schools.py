import csv
import json

schools = None

with open('schools.json', 'rb') as jsonfile:
    schools = json.load(jsonfile)

with open('table.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)

    with open('output.csv', 'wb') as outputfile:
        writer = csv.DictWriter(outputfile, fieldnames=reader.fieldnames)
        for row in reader:
            if row["school"]:
                name = schools.get(row["school"].lower().strip(), "")
                if name != "":
                    row["school"] = name
            writer.writerow(row)

