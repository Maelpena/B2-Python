#!/usr/bin/env python36

import argparse

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


ma_liste=[4,5,2,3,4]

if args.list:
  print(ma_liste)

elif (args.ajout != None):
  ma_liste = ma_liste + args.ajout
  print(ma_liste)

elif args.suppr:
  while ma_liste != []:
    i=0
    del ma_liste[i]
    i += 1
  print(ma_liste)

elif args.option:

  if args.max:   
    print("La valeur maximale de la liste est",max(ma_liste))

  elif args.min:
    print("La valeur minimale de la liste est", min(ma_liste))

  elif args.moy:
    i = 0
    somme = 0
    moy = 0
    while i != len(ma_liste):
      somme += int(ma_liste[i])
      i += 1
    moy = somme/len(ma_liste)
    print("La moyenne de la liste est",moy)

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
