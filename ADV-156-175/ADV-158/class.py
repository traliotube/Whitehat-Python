from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Geometry Error")
root.geometry('400x400')
input = Entry(root)
input.pack()


def addition():
    try:
        print(5+int(input.get()))
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")


btn = Button(root, text="Add", command=addition)
btn.pack()

root.mainloop()
