import csv
import random
import sys
csvfile = open('D:\Dev\OpenClassRoom\CSV.csv','w',encoding='UTF8',newline='')
writer = csv.writer(csvfile)
listeCSV = []

while len(listeCSV) <= 20:
    quantité = random.choice([round(random.uniform(0,9000),1),random.randrange(0,9000,1)])
    unité = random.choice(["h","s","m"])
    row = (quantité,unité)
    listeCSV.append(row)
    writer.writerow(listeCSV[-1])
