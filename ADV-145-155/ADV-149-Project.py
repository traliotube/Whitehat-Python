from tkinter import *
from random import randint

root = Tk()
root.title("Random Word Generator")
root.geometry('300x300')
root.configure(background='skyblue')

radomWord = Label(root)


def randomListGenerator():
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    randomItem1 = list[randint(0, 25)]
    randomItem2 = list[randint(0, 25)]
    randomItem3 = list[randint(0, 25)]
    randomItem4 = list[randint(0, 25)]
    randomItem5 = list[randint(0, 25)]
    radomWord["text"] = f"The random word is {randomItem1}{randomItem2}{randomItem3}{randomItem4}{randomItem5}"


btn = Button(root, text="Generate List",
             command=randomListGenerator, fg="black", bg="lightgreen")

btn.place(relx=0.5, rely=0.3, anchor=CENTER)
radomWord.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
