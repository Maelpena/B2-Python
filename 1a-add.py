#!/usr/bin/env python36

import re

patern = re.compile('^[0-9]*$')

nbr1 = input('premier nombre a ajouter : ')

if patern.match(nbr1):

  nbr2 = input('deuxieme nombre a ajouter : ')

  if patern.match(nbr2):
    nbr1 = int(nbr1)
    nbr2 = int(nbr2)
    somme = nbr1 + nbr2
    print (somme)

  else:
    print ("ce n'est pas un chiffre")

else:
  print ("ce n'est pas un chiffre")
