from tkinter import *
from random import randint

root = Tk()
root.title("Luck Friend Wheel")
root.geometry('400x400')
root.configure(bg="skyblue")

nameInput = Entry(root, text="Enter your friend's name")
nameInput.place(relx=0.5, rely=0.2, anchor=CENTER)

friendList = Label(root)
randomNumberLabel = Label(root)
luckyFriend = Label(root)


list = []


def addFriend():
    friend = nameInput.get()
    list.append(friend)
    friendList["text"] = list
    nameInput.delete(0, END)


def randomNumber():
    randomNumber = randint(0, len(list)-1)
    randomNumberLabel["text"] = f"The random number is {randomNumber}!"
    randomFriend = list[randomNumber]
    luckyFriend["text"] = f"Your lucky friend is {randomFriend}!"


addFriendBtn = Button(root, text="Add Friend",
                      command=addFriend, bg="yellow", fg="black")
randomFriendBtn = Button(root, text="Click to know your lucky friend",
                         command=randomNumber, bg="yellow", fg="black")

addFriendBtn.place(relx=0.5, rely=0.3, anchor=CENTER)
friendList.place(relx=0.5, rely=0.4, anchor=CENTER)
randomFriendBtn.place(relx=0.5, rely=0.5, anchor=CENTER)
randomNumberLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
luckyFriend.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
