from tkinter import *
from random import randint

root = Tk()
root.title("TESTING RANDOM FUNCTION")
root.geometry('300x300')

guessedLabel = Label(root)
generatedLabel = Label(root)
input = Entry(root)

array = [[["A", "B", "C", "D", "E", "F", "G", "H"], ["King", "Queen"],
          ["!", "@", "#", "$", "%", "^", "&", "*"]]]


def guessPassword():
    randNo1 = randint(0, 7)
    randNo2 = randint(0, 1)
    randNo3 = randint(0, 7)

    letter1 = array[0][0][randNo1]
    letter2 = array[0][1][randNo2]
    letter3 = array[0][2][randNo3]

    guessedLabel["text"] = "Guessed Password: " + input.get()
    generatedLabel["text"] = f"Generated Password: {letter1}{letter2}{str(letter3)}"


btn = Button(root, text="Guess Password", command=guessPassword)

input.place(relx=0.5, rely=0.3, anchor=CENTER)
guessedLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
generatedLabel.place(relx=0.5, rely=0.6, anchor=CENTER)


root.mainloop()
