from finder import *

#je sais pas pourquoi mais si je le met pas ça ne marche pas 
actuelle = [1]

#liste traitée avtuellement
res = []

#liste de toutes les possibilités
final = []

while len(res) <= 3:
  res=incrémenter(actuelle)
  if pasdouble(res) and legite(res):
    print(res)
  actuelle = res