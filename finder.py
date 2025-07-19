from typing import List

matrice = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

actuelle = [1]

def incrémenter(tab:List[int]):
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
  if len(tab) == len(list(set(tab))):
    return True
  return False

def legite(tab:List[int]):
  i = 0
  précedent = []
  while i+1<len(tab):
    if tab[i]==1:
      if not 2 in précedent and 3 == tab[i+1]:
        return False
      elif not 4 in précedent and 7 == tab[i+1]:
        return False
      elif not 5 in précedent and 9 == tab[i+1]:
        return False
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
      elif not (tab[i+1] in [1,2,3,4,7,8,9]):
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
    
    précedent.append(tab[i])
    i+=1
  return True
        

e=0
while e<=1000:
  res=incrémenter(actuelle)
  if pasdouble(res) and legite(res):
    print(res)
  actuelle = res
  e+=1