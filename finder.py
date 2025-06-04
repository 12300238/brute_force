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

e=0
while e<=1000:
    res=incrémenter(actuelle)
    if pasdouble(res):
        print(res)
    actuelle = res
    e+=1