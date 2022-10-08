from tkinter import *
root = Tk()
root.title("Dictionary")
root.geometry('400x400')

mutableLabel = Label(root)
immutableLabel = Label(root)
tkinterLabel = Label(root)

dictionary = {
    "Mutable": "Values can be changed",
    "Immutable": "Values cannot be changed",
    "Tkinter": "A GUI library for python",
}


def mutable():
    mutableLabel["text"] = dictionary["Mutable"]


def immutable():
    immutableLabel["text"] = dictionary["Immutable"]


def tkinter():
    tkinterLabel["text"] = dictionary["Tkinter"]


mutableButton = Button(root, text="Meaning of Mutable", command=mutable)
immutableButton = Button(root, text="Meaning of Immutable", command=immutable)
tkinterButton = Button(root, text="Meaning of Tkinter", command=tkinter)

mutableButton.place(relx=0.5, rely=0.2, anchor=CENTER)
mutableLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
immutableButton.place(relx=0.5, rely=0.4, anchor=CENTER)
immutableLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
tkinterButton.place(relx=0.5, rely=0.6, anchor=CENTER)
tkinterLabel.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
