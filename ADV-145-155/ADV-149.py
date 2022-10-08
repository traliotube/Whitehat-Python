from tkinter import *
from random import randint

root = Tk()
root.title("Luck Friend Wheel")
root.geometry('300x300')

list = ["Aadarsh", "Aaron", "Murali", "Ayan", "Rishi"]
print(list)


def randomNumber():
    randomNumber = randint(0, len(list)-1)
    print(randomNumber)
    randomFriend = list[randomNumber]
    print(f"Your lucky friend is {randomFriend}")


btn = Button(root, text="Click to know your lucky friend",
             command=randomNumber)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

root.mainloop()
