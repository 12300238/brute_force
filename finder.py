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
  while i+1<len(tab):
    if tab[i]==1 and not (tab[i+1] in [2,4,5]):
      return False
    elif tab[i]==2 and not (tab[i+1] in [1,4,5,6,3]):
      return False
    elif tab[i]==3 and not (tab[i+1] in [2,5,6]):
      return False
    elif tab[i]==4 and not (tab[i+1] in [1,2,5,8,7]):
      return False
    elif tab[i]==5 and not (tab[i+1] in [1,2,3,4,6,8,7,9]):
      return False
    elif tab[i]==6 and not (tab[i+1] in [2,3,5,8,9]):
      return False
    elif tab[i]==7 and not (tab[i+1] in [4,5,8]):
      return False
    elif tab[i]==8 and not (tab[i+1] in [7,4,5,6,9]):
      return False
    elif tab[i]==9 and not (tab[i+1] in [8,5,6]):
      return False
    i+=1
  return True
        

e=0
while e<=100:
  res=incrémenter(actuelle)
  if legite(res):
    print(res)
  actuelle = res
  e+=1