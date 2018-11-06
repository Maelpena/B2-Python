#!/usr/bin/env python36

compt=0
list = []
list.append(input("prenom 1 : "))
while list[compt] != "q":
  list.append(input("prenom suivant : "))
  compt += 1


del list[compt]
list.sort()
print(list)

