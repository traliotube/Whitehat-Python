from tkinter import *
from random import randint

root = Tk()
root.title("Random Colour")
root.geometry('400x400')

dictionary = {"Colour": ["maroon1", "lawn green", "magenta2",
                         "purple1", "springgreen2", "chocolate1", "deep pink", "cyan"]}


def randomColour():
    randomColour = dictionary["Colour"][randint(
        0, len(dictionary["Colour"])-1)]
    root.config(bg=randomColour)
    print(randomColour)


btn = Button(root, text="Set Background as Random Colour",
             command=randomColour)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
