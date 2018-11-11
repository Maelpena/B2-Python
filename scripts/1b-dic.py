#!/usr/bin/env python36

#1b-dic.py
#Mael PENA
#11 nov 2018


import re

pattern = re.compile('^([a-z]|[A-Z])*$')

compt=0
list = []

var = input("prenom 1 : ")

if pattern.match(var):
  list.append(var)
  while list[compt] != "q":
    var = input("prenom suivant : ")
    if pattern.match(var):
      list.append(var)
      compt += 1
    else:
      print("Cela n'est pas un prenom")
else:
  print ("ce n'est pas un prenom")


del list[compt]
list.sort()
print(list)

