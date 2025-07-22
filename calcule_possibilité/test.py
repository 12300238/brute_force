from finder import *

while len(res) <= 3:
  res=incrémenter(actuelle)
  if pasdouble(res) and legite(res):
    print(res)
  actuelle = res