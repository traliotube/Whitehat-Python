from tkinter import *
from random import sample

root = Tk()
root.title("List")
root.geometry('300x300')

randomList = Label(root)
sortedList = Label(root)

def randomListGenerator():
    list = sample(range(10,30), 5)
    randomList["text"] = f"Random List: {list}"
    list.sort()
    sortedList["text"] = f"Sorted List: {list}"
 
btn = Button(root, text="Generate List", command=randomListGenerator)

btn.place(relx = 0.5, rely = 0.3, anchor=CENTER)
randomList.place(relx = 0.5, rely = 0.4, anchor=CENTER)
sortedList.place(relx = 0.5, rely = 0.5, anchor=CENTER)


root.mainloop()
