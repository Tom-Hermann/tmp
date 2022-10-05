import csv
csvfile1 = open('CIS_Innuendo.csv', 'r')
spamreader1 = csv.DictReader(csvfile1, delimiter='\t')

i = 0
for row in spamreader1:
    for i in row['Denomunation_substance']:
        print(i, ord(i))
    break
csvfile1.close()