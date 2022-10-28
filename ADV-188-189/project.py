import hashlib
from tkinter import *
from tkinter.messagebox import showinfo
from firebase import firebase

registrationWindow = Tk()
registrationWindow.geometry("400x400")

firebase = firebase.FirebaseApplication(
    "https://logincredentials-c188-189-default-rtdb.asia-southeast1.firebasedatabase.app/", None)


def login():
    print("login function")


def register():
    global usernameEntry
    global passwordEntry

    password = hashlib.md5(passwordEntry.get().encode()).hexdigest()
    firebase.put("/", usernameEntry.get(), password)
    showinfo("Success", "Registered Successfully")
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)


def loginWindow():
    global loginUsernameEntry
    global loginPasswordEntry

    loginWindow = Tk()
    loginWindow.geometry("400x400")

    log_heading_label = Label(loginWindow, text="Log In", font='arial 18 bold')
    log_heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

    login_username_label = Label(
        loginWindow, text="Username : ", font='arial 13')
    login_username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

    loginUsernameEntry = Entry(loginWindow)
    loginUsernameEntry.place(relx=0.6, rely=0.4, anchor=CENTER)

    login_password_label = Label(
        loginWindow, text="Password : ", font='arial 13')
    login_password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

    loginPasswordEntry = Entry(loginWindow)
    loginPasswordEntry.place(relx=0.6, rely=0.5, anchor=CENTER)

    btn_login = Button(loginWindow, text="Log In",
                       font='arial 13 bold', command=login, relief=FLAT)
    btn_login.place(relx=0.5, rely=0.65, anchor=CENTER)
    registrationWindow.destroy()
    loginWindow.mainloop()


heading_label = Label(registrationWindow,
                      text="Register", font='arial 18 bold')
heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

username_label = Label(registrationWindow, text="Username : ", font='arial 13')
username_label.place(relx=0.3, rely=0.4, anchor=CENTER)

usernameEntry = Entry(registrationWindow)
usernameEntry.place(relx=0.6, rely=0.4, anchor=CENTER)

password_label = Label(
    registrationWindow, text="Password :  ", font='arial 13')
password_label.place(relx=0.3, rely=0.5, anchor=CENTER)

passwordEntry = Entry(registrationWindow)
passwordEntry.place(relx=0.6, rely=0.5, anchor=CENTER)

btn_reg = Button(registrationWindow, text="Sign Up",
                 font='arial 13 bold', command=register, relief=FLAT, padx=10)
btn_reg.place(relx=0.5, rely=0.75, anchor=CENTER)

btn_login_window = Button(registrationWindow, text="Log In",
                          font='arial 10 bold',  command=loginWindow, relief=FLAT)

btn_login_window.place(relx=0.9, rely=0.06, anchor=CENTER)
registrationWindow.mainloop()
