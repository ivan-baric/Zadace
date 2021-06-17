from csv import reader

with open('rezultati.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_tuples = list(map(tuple, csv_reader))

sortirano = sorted(list_of_tuples, key=lambda x: x[1])
print(sortirano)
print("-------------------------------")

rjecnik = {
    'nedovoljan': 0,
    'dovoljan': 0,
    'dobar': 0,
    'vrlodobar': 0,
    'izvrstan': 0,
}

for ucenik in sortirano:
    if int(ucenik[2]) >= 0 and int(ucenik[2]) <= 49:
        rjecnik['nedovoljan'] = int(rjecnik['nedovoljan']) + 1
    elif int(ucenik[2]) >= 50 and int(ucenik[2]) <= 65:
        rjecnik['dovoljan'] = int(rjecnik['dovoljan']) + 1
    elif int(ucenik[2]) >= 66 and int(ucenik[2]) <= 80:
        rjecnik['dobar'] = int(rjecnik['dobar']) + 1
    elif int(ucenik[2]) >= 81 and int(ucenik[2]) <= 90:
        rjecnik['vrlodobar'] = int(rjecnik['vrlodobar']) + 1
    elif int(ucenik[2]) >= 91 and int(ucenik[2]) <= 100:
        rjecnik['izvrstan'] = int(rjecnik['izvrstan']) + 1

print(rjecnik)
