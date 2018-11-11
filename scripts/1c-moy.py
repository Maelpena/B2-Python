#!/usr/bin/env python36

#1c-moy.py
#Mael PENA
#11 nov 2018


import re

patt = re.compile('^([a-z]|[A-Z])*$')
pat = re.compile('^[0-9]*$')

dico={}
prenom=""
while prenom != "q":

  prenom = input("Quel est son prenom ?")
  if prenom == "q":
    break  
  elif patt.match(prenom):
    note = input("Quel est sa note ?")
    if note == "q":
      break
    elif pat.match(note):
      dico[prenom]=note
    else:
      print ("ce n'est pas une note, veuillez rentrer le prenom")
  else:
    print ("ce n'est pas un prenom")

print (dico)

