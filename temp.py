import csv
fields = []
description = {}

with open(r'C:/Users/abhis/Desktop/chat-app/AI-Doctor/ml/disease_description.csv',encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        disease, desc = row
        description[disease] = desc
    
print(description)
