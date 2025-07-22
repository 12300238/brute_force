from time import sleep
from pynput.mouse import Controller, Button
from pynput import mouse

souris = Controller()

def co_finder(i:int) -> list[int]:
    '''
    Retourne les coordonnées du point i sur le schéma
    '''
    # Coordonnées des points sur le schéma
    coords = {
        1: [2243, 1185],
        2: [2364, 1185],
        3: [2481, 1185],
        4: [2243, 1305],
        5: [2364, 1305],
        6: [2481, 1305],
        7: [2243, 1423],
        8: [2364, 1423],
        9: [2481, 1423]
    }
    return coords.get(i, [0, 0])  # Retourne [0,0] si i n'est pas valide
