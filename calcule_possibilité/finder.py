from typing import List
import json

def incrémenter(tab:List[int]):
  '''
  augmente la valeur du premier élément de la liste de 1, et gère les retenues si nécessaire
  
  param tab: liste a incrémenter
  retourne: la liste incrémentée
  '''
  tab[0] +=1
  i=0
  while i < len(tab)-1:
    if tab[i] == 10:
      tab[i]=1
      tab[i+1]+=1
    i+=1
  if tab[len(tab)-1] == 10:
    tab[len(tab)-1] = 1
    tab.append(1)
  return tab

def pasdouble(tab:List[int]):
  '''
  vérifie si la liste ne contient pas de doublons

  param tab: liste a vérifier
  retourne: True si pas de doublons, False sinon
  '''
  if len(tab) == len(list(set(tab))):
    return True
  return False

def legite(tab:List[int]):
  '''
  vérifit si la l'enchainement est possible a reproduire sur le chema

  param tab: liste a vérifier
  retourne: True si l'enchainement est possible, False sinon
  '''

  i = 0
  précedent = []

  while i+1<len(tab):
    if tab[i]==1:
      #si un nombre est déjà pris alors on peut accéder a celui derière
      if not 2 in précedent and 3 == tab[i+1]:
        return False
      elif not 4 in précedent and 7 == tab[i+1]:
        return False
      elif not 5 in précedent and 9 == tab[i+1]:
        return False
      #si le nombre suivant est accessible directement
      elif not (tab[i+1] in [2,4,5,8,6]):
        return False
      
    elif tab[i]==2:
      if not 5 in précedent and 8 == tab[i+1]:
        return False
      elif not (tab[i+1] in [1,3,4,5,6,7,9]):
        return False
      
    elif tab[i]==3:
      if not 2 in précedent and 1 == tab[i+1]:
        return False
      elif not 6 in précedent and 9 == tab[i+1]:
        return False
      elif not 5 in précedent and 7 == tab[i+1]:
        return False
      elif not (tab[i+1] in [2,4,5,8,6]):
        return False
      
    elif tab[i]==4:
      if not 5 in précedent and 6 == tab[i+1]:
        return False
      elif not (tab[i+1] in [1,2,3,5,7,8,9]):
        return False
      
    elif tab[i]==6:
      if not 5 in précedent and 4 == tab[i+1]:
        return False
      elif not (tab[i+1] in [1,2,3,5,7,8,9]):
        return False
      
    elif tab[i]==7:
      if not 4 in précedent and 1 == tab[i+1]:
        return False
      elif not 8 in précedent and 9 == tab[i+1]:
        return False
      elif not 5 in précedent and 3 == tab[i+1]:
        return False
      elif not (tab[i+1] in [2,4,5,8,6]):
        return False
      
    elif tab[i]==8:
      if not 5 in précedent and 2 == tab[i+1]:
        return False
      elif not (tab[i+1] in [1,3,4,5,6,7,9]):
        return False
      
    elif tab[i]==9:
      if not 6 in précedent and 3 == tab[i+1]:
        return False
      elif not 5 in précedent and 1 == tab[i+1]:
        return False
      elif not 8 in précedent and 7 == tab[i+1]:
        return False
      elif not (tab[i+1] in [2,4,5,8,6]):
        return False
    
    #la liste de tout les nombres déjà traité dans le tableau actuel
    précedent.append(tab[i])
    i+=1

  return True

#je sais pas pourquoi mais si je le met pas ça ne marche pas 
actuelle = [1]

#liste traitée avtuellement
res = []

#liste de toutes les possibilités
final = []