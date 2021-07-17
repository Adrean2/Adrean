import sys
import os
import csv
from Conversion import conversion

if __name__ == '__main__':
  with open('D:\Dev\$ COURS OPEN CLASSROOMS\Exercices\Temps\CSV.csv','r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
      durée = float(line[0])
      unité = str(line[1])
      conversion(durée,unité)