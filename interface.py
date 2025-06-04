from tkinter import *

def do_something():
    print("Clicked")


# On instancie notre fenêtre graphique
window = Tk()

# On injecte un premier label dans la fenêtre
label = Label(window, text="Hello Tk")
label.pack()

# Puis, on injecte un bouton dans la fenêtre. Il est connecté à la
# fonction do_something qui déclenchera au clic sur le bouton.
button = Button(window, text="Push me !", command=do_something)
button.pack()

window.mainloop()