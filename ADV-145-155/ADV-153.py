from tkinter import *
from random import randint

root = Tk()
root.title("Password Generator")
root.geometry('400x400')

label = Label(root)

array = [[[1, 2, 3, 4, 5, 6], ["Head", "Tail"],
          ["A", "B", "C", "D", "E", "F", "G", "H"]]]
print(array[0][2][3])


def passwordGen():
    randNo1 = randint(0, 5)
    randNo2 = randint(0, 1)
    randNo3 = randint(0, 7)

    letter1 = array[0][0][randNo1]
    letter2 = array[0][1][randNo2]
    letter3 = array[0][2][randNo3]

    label["text"] = str(letter1) + letter2 + letter3


btn = Button(root, text="Generate Password", command=passwordGen)

btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
