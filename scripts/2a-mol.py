#!/usr/bin/env python36

from os import chdir
chdir("/home/maelpena/B2-Python")

f = open("fichiertexte", "w")
f.write(input("insert un nombre entre 1 et 100 : "))

import random
r = random.randint(0,100)

f = open("fichiertexte", "r")
nombre = int(f.read())

while nombre != "q":
  if (r < nombre):
    f = open("fichiertexte", "w")
    f.write("cest moins")
    f = open("fichiertexte", "w")
    f.write(input("insert un nombre entre 1 et 100 : "))
    f = open("fichiertexte", "r")
    nombre = int(f.read())
    f.close()
  elif (r > nombre):
    f = open("fichiertexte", "w")
    f.write("c'est plus")
    f = open("fichiertexte", "w")
    f.write(input("insert un nombre entre 1 et 100 : "))
    f = open("fichiertexte", "r")
    nombre = int(f.read())
    f.close()
  else:
    f = open("fichiertexte", "w")
    f.write("touver")
    sys.exit()
    f.close()
    
