from tkinter import *
from random import randint

root = Tk()
root.title("List")
root.geometry('600x300')

randomList = Label(root)
sortedList = Label(root)


def randomItemGenerator():
    list = ["a picnic basket or cooler",
            "a blanket",
            "plates and cups",
            "food",
            "sunscreen"]
    randomList["text"] = f"Picnic List: {list}"
    randomNumber = int(randint(0, len(list)-1))
    sortedList["text"] = f"Put {list[randomNumber]} in bag"


btn = Button(root, text="Which item shall I put in my bag?",
             command=randomItemGenerator, bg="yellow", fg="black")

randomList.place(relx=0.5, rely=0.3, anchor=CENTER)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
sortedList.place(relx=0.5, rely=0.5, anchor=CENTER)


root.mainloop()
