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

def click_and_move(possibility:list[int], pos=souris.position):

    co = co_finder(possibility[0])
    souris.position = (co[0], co[1])
    pos = souris.position
    sleep(0.01)

    i=1
    souris.press(Button.left)
    while i< len(possibility):
        co = co_finder(possibility[i])
        souris.move(co[0]-pos[0], co[1]-pos[1])
        pos = co
        sleep(0.01)
        i += 1
    souris.release(Button.left)