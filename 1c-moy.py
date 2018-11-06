!/usr/bin/env python36

dico={}
prenom=""
while prenom != "q":
  prenom=input("Quel est son prenom ?")
  if prenom == "q":
    break
  note=input("Quel est sa note ?")
  dico[prenom]=note

print (dico)

