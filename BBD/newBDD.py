import csv

csvfile1 = open('CIS_bdpm.txt', 'r')
fieldnames = ['CIS', 'Nom', 'Forme_pharmaceutique', "Voies_d'administration"]
# spamreader1 = csv.reader(csvfile1, delimiter='\t', quotechar='|')
spamreader1 = csv.DictReader(csvfile1, delimiter='\t')


csvfile2 =  open('CIS_COMPO_bdpm.txt', 'r')
    # spamreader2 = csv.reader(csvfile2, delimiter='\t', quotechar='|')
spamreader2 = csv.DictReader(csvfile2, delimiter='\t')

i = 0
Denomunation_substance = {}
# for row in spamreader1:
#     print(row['CIS'], row['Nom'])
#     i += 1
#     if (i ==4):
#         break
# i = 0
for row in spamreader2:
    Denomunation_substance[row['CIS']] = row['Denomunation_substance']

print(len(Denomunation_substance))



csv_columns = ['CIS', 'Nom', 'Denomunation_substance']
dict_data = [
{'No': 1, 'Name': 'Alex', 'Country': 'India'},
{'No': 2, 'Name': 'Ben', 'Country': 'USA'},
{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
{'No': 4, 'Name': 'Smith', 'Country': 'USA'},
{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
]
csv_file = "CIS_Innuendo.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter='\t')
        writer.writeheader()
        for row in spamreader1:
            new_row = {}
            new_row['CIS']=row['CIS']
            new_row['Nom']=row['Nom']
            try:
                new_row['Denomunation_substance'] = Denomunation_substance[row['CIS']]
            except:
                print('error')
                continue
            writer.writerow(new_row)
except IOError:
    print("I/O error")


csvfile1.close()
csvfile2.close()
