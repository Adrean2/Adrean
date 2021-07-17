import sys
import os
import csv
import random

<<<<<<< HEAD
def create_csv():
    # Création fichier CSV
    with open('D:\Dev\$ COURS OPEN CLASSROOMS\ProjetTemps\CSV.csv','w',encoding='UTF8',newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Ajout de données dans le fichier CSV
        listeCSV = []
        while len(listeCSV) <= 20:
            # choisit entre une quantité float ou int, de 0 à 9000
            quantité = random.choice([round(random.uniform(0,9000),1),random.randrange(0,9000,1)])
            if quantité >= 30:
                unité = random.choice(["s","m"])
            else:
                unité = random.choice(["h","s","m"])
            row = (quantité,unité)
            listeCSV.append(row)
            writer.writerow(listeCSV[-1])
=======
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
    
>>>>>>> 7d617fa7cc0e1a849c85bf000889591caf4a6853
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
<<<<<<< HEAD
    create_csv()
    with open('D:\Dev\$ COURS OPEN CLASSROOMS\ProjetTemps\CSV.csv','r',encoding='UTF8') as csv_reader:
        reader  = csv.reader(csv_reader,delimiter=",")
        for line in reader:
            durée = float(line[0])
            unité = str(line[1])
            conversion(durée,unité)
=======
  with open('D:\Dev\$ COURS OPEN CLASSROOMS\ProjetTemps\CSV.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
      durée = float(line[0])
      unité = str(line[1])
      conversion(durée,unité)
>>>>>>> 7d617fa7cc0e1a849c85bf000889591caf4a6853
