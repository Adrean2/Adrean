import sys
import os
import csv
import random

# Création fichier CSV
csvfile = open('D:\Dev\$ COURS OPEN CLASSROOMS\ProjetTemps\CSV.csv','w',encoding='UTF8',newline='')
writer = csv.writer(csvfile)

# Ajout de données dans le fichier CSV
listeCSV = []
while len(listeCSV) <= 20:
    quantité = random.choice([round(random.uniform(0,9000),1),random.randrange(0,9000,1)])
    unité = random.choice(["h","s","m"])
    row = (quantité,unité)
    listeCSV.append(row)
    writer.writerow(listeCSV[-1])
# Création conversion de la durée
def conversion(durée,unité):
    h = 0
    m = 0
    s = 0
    # Conversion en secondes (unité la plus basse)
    if unité == "h":
        durée = durée*3600
    elif unité == "m":
        durée = durée*60
    elif unité == "s":
        pass
    else:
        print("Erreur d'unité")
    # incrémentation des heures, minutes, le restant étant les secondes
    while durée >= 3600:
        h += 1
        durée -= 3600

    while durée >= 60:
        m += 1
        durée -= 60

    s = int(durée)

    # Mise en forme/affichage du résultat final
    print("{} heures,{} minutes,{} secondes.".format(h,m,s))

if __name__ == '__main__':
  with open('D:\Dev\$ COURS OPEN CLASSROOMS\ProjetTemps\CSV.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
      durée = float(line[0])
      unité = str(line[1])
      conversion(durée,unité)