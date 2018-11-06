#!/usr/bin/env python36

import sys
import signal
def quitter(r):
  r = str(r)
  print ("au revoir, la bonne reponse était " + r)

import random
r = random.randint(0,100)

nombre = (input())
while nombre != "q":
  nombre = int(nombre)
  if (r < nombre):
    print ("cest moins")
  elif (r > nombre):
    print ("cest plus")
  else:
    print ("touver")
    sys.exit()
  nombre = input()

quitter(r)

