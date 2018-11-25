#!/usr/bin/env python36

import argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--list", help="Affiche la liste",action="store_true")
parser.add_argument("-a", "--ajout",help="Ajoute les elements dans la liste",type=int, nargs='+')
parser.add_argument("-c", "--suppr",help="Supprime les elements de la liste", action="store_true")
parser.add_argument("-s", "--option", help="Permet d'executer les differentes options suivantes : --max --min --moy --sum", action="store_true")
parser.add_argument("--max", help="Affiche la valeur maximale de la liste", action="store_true")
parser.add_argument("--min", help="Affiche la valeur minimale de la liste", action="store_true")
parser.add_argument("--moy", help="Affiche la moyenne de tous les elements de la liste", action="store_true")
parser.add_argument("--sum", help="Affiche la somme de tous les elements de la liste", action="store_true")
parser.add_argument("-t", "--trie", help="Trie les elements de la liste dans l'ordre croissant", action="store_true")
parser.add_argument("--desc", help="Trie les element de la liste dans l'ordre decroissant", action="store_true")

args = parser.parse_args()


if args.list:
  with open ("ma_liste.csv", "r") as ma_liste:
    reader = csv.reader(ma_liste)
    for row in reader:
      print(' '.join(row))


elif (args.ajout != None):
  with open ("ma_liste.csv", "a") as ma_liste:
    writer = csv.writer(ma_liste)
    writer.writerows([a] for a in args.ajout)
  

elif args.suppr:

  truncate_list = open("ma_liste.csv", "w+")
  truncate_list.close()

elif args.option:

  if args.max:   

    with open('ma_liste.csv', 'r') as ma_liste:
      reader = csv.reader(ma_liste)

      tab = []

      for row in reader:
        for var in row:
          var = int(var)
          tab.append(var)

      maxi = max(tab)
      print(maxi)

  elif args.min:

      with open('ma_liste.csv', 'r') as ma_liste:
        reader = csv.reader(ma_liste)

        tab = []
        
        for row in reader:
          for var in row:
            var = int(var)
            
            tab.append(var)
        mini = min(tab)
        print(mini)


  elif args.moy:


    with open('ma_liste.csv', 'r') as ma_liste:
      reader = csv.reader(ma_liste)
      tab = []
      for row in reader:
        for var in row:
          var = int(var)
          tab.append(var)        

      moyenne = sum(ma_liste)/len(ma_liste)
      print(len(ma_liste))


  elif args.sum:
    i = 0
    somme = 0
    while i != len(ma_liste):
      somme += int(ma_liste[i])
      i += 1
    print("La somme des elements de la liste est de", somme)


elif args.trie:
  ma_liste.sort()
  if args.desc:   
    ma_liste.reverse()
  print(ma_liste)
