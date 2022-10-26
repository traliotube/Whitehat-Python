import firebase
from tkinter import *
from simplecrypt import encrypt, decrypt

firebase = firebase.FirebaseApplication(
    "https://encryptedchat-165c8-default-rtdb.asia-southeast1.firebasedatabase.app", None)

loginWindow = Tk()
loginWindow.geometry("400x400")
loginWindow.config(bg='AB92BF')


def sendData():
    global username
    global userCode
    global messageEntry
    message = f"{username}: {messageEntry.get()}"
    cipherCode = encrypt("Password", message).hex()
    put = firebase.put("/", userCode, cipherCode)
    print(put)


def enterRoom():
    global username
    global userCode
    global friendCode
    global messageEntry
    global messageText
    userCode = userCodeEntry.get()
    friendCode = friendCodeEntry.get()
    username = usernameEntry.get()
    sendData()
    loginWindow.destroy()

    messageWindow = Tk()
    messageWindow.config(bg='AFC1D6')
    messageWindow.geometry("600x500")

    messageText = Text(messageWindow, height=20, width=72)
    messageText.place(relx=0.5, rely=0.35, anchor=CENTER)

    messageLabel = Label(messageWindow, text="Message ",
                         font='arial 13', bg='AFC1D6', fg="white")
    messageLabel.place(relx=0.3, rely=0.8, anchor=CENTER)

    messageEntry = Entry(messageWindow, font='arial 15')
    messageEntry.place(relx=0.6, rely=0.8, anchor=CENTER)

    btnSend = Button(messageWindow, text="Send", font='arial 13',
                     bg="D6CA98", fg="black", padx=10, relief=FLAT)
    btnSend.place(relx=0.5, rely=0.9, anchor=CENTER)

    messageWindow.mainloop()


username_label = Label(loginWindow, text="Username : ",
                       font='arial 13', bg='AB92BF', fg="white")
username_label.place(relx=0.3, rely=0.3, anchor=CENTER)

usernameEntry = Entry(loginWindow)
usernameEntry.place(relx=0.6, rely=0.3, anchor=CENTER)

your_code_label = Label(loginWindow, text="Your code :  ",
                        font='arial 13', bg='AB92BF', fg="white")
your_code_label.place(relx=0.3, rely=0.4, anchor=CENTER)

userCodeEntry = Entry(loginWindow)
userCodeEntry.place(relx=0.6, rely=0.4, anchor=CENTER)

friends_code_label = Label(
    loginWindow, text="Your Friends code :  ", font='arial 13', bg='AB92BF', fg="white")
friends_code_label.place(relx=0.22, rely=0.5, anchor=CENTER)

friendCodeEntry = Entry(loginWindow)
friendCodeEntry.place(relx=0.6, rely=0.5, anchor=CENTER)

btn_start = Button(loginWindow, text="Start", font='arial 13',
                   bg="CEF9F2", fg="black", command=enterRoom, relief=FLAT, padx=10)
btn_start.place(relx=0.5, rely=0.65, anchor=CENTER)


loginWindow.mainloop()
