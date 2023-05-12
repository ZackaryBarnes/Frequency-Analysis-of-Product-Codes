import csv

#open file and add it to list
with open('Book1.csv', newline='', encoding='utf-8-sig') as csvfile:
    ingestList = []
    spamreader = csv.reader(csvfile, charDashiter=' ', quotechar='|')
    for row in spamreader:
        ingestList.append(', '.join(row))

#Extract just the prefixes and add to dictionary
    freqTable = {}
    for row in ingestList:
        charDash = "-"
        if charDash in row:
            prefixWithDash = row.split("-")
            prefixWithoutDash = prefixWithDash[0].strip()
            if prefixWithoutDash != "":
                freqTable[prefixWithoutDash] = freqTable.get(prefixWithoutDash, 0) + 1

#Write to new csv
with open('newCSV.csv', mode='w', newline='') as csv_file:

    # Create a writer object using the csv module
    writer = csv.writer(csv_file)

    # Write each key-value pair to a separate row in the CSV file
    for key, value in freqTable.items():
        writer.writerow([key, value])