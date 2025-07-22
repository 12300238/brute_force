from time import sleep
from pynput.mouse import Controller, Button

mouse = Controller()

mouse.press(Button.left)
mouse.move(100, 0)
sleep(0.1)
mouse.move(0, 100)
sleep(0.1)
mouse.move(-100, 0)
mouse.release(Button.left)