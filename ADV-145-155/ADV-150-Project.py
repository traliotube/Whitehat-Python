from tkinter import *
from random import randint

root = Tk()
root.title("Random Countries and Capitals")
root.geometry('500x500')
root.configure(bg="skyblue")

countryInput = Entry(root)
countryInput.place(relx=0.5, rely=0.2, anchor=CENTER)
capitalInput = Entry(root)
capitalInput.place(relx=0.5, rely=0.2, anchor=CENTER)

countryListLabel = Label(root)
capitalListLabel = Label(root)
randomCountry = Label(root)
randomCapital = Label(root)


countryList = []
capitalList = []


def addCountryAndCapital():
    countryList.append(countryInput.get())
    countryListLabel["text"] = f"The list of countries entered are {countryList}"
    countryInput.delete(0, END)
    capitalList.append(capitalInput.get())
    capitalListLabel["text"] = f"The list of capitals entered are {capitalList}"
    capitalInput.delete(0, END)


def randomNumber():
    randomNumber = randint(0, len(countryList)-1)
    randomCountry["text"] = f"The random country is {countryList[randomNumber]}!"
    randomCapital["text"] = f"The {countryList[randomNumber]}'s capital is {capitalList[randomNumber]}!"


addFriendBtn = Button(root, text="Add Country and Capital",
                      command=addCountryAndCapital, bg="yellow", fg="black")
randomFriendBtn = Button(root, text="Click to get a random country with it's capital",
                         command=randomNumber, bg="yellow", fg="black")

countryInput.place(relx=0.5, rely=0.1, anchor=CENTER)
capitalInput.place(relx=0.5, rely=0.2, anchor=CENTER)
addFriendBtn.place(relx=0.5, rely=0.3, anchor=CENTER)
randomFriendBtn.place(relx=0.5, rely=0.4, anchor=CENTER)
countryListLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
capitalListLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
randomCountry.place(relx=0.5, rely=0.7, anchor=CENTER)
randomCapital.place(relx=0.5, rely=0.8, anchor=CENTER)


root.mainloop()
