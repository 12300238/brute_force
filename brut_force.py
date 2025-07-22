from time import sleep
from calcule_possibilité.finder import pasdouble, incrémenter, legite
from sourie.execution_possibilite import click_and_move

actuelle = [1]

#liste traitée avtuellement
res = []

#liste de toutes les possibilités
final = []

while len(res) <= 3:
  res=incrémenter(actuelle)
  if pasdouble(res) and legite(res):
    click_and_move(res)
    sleep(0.5)
  actuelle = res