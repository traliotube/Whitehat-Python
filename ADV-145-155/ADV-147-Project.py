from tkinter import *

root = Tk()
root.title("ASCII")
root.geometry('300x300')

inputBox = Entry(root)
inputBox.place(relx=0.5, rely=0.2, anchor=CENTER)

asciiLabel = Label(root, text="Text in ASCII: ")
encryptedLabel = Label(root, text="Encrypted Text: ")


def asciiConverter():
    asciiLabel["text"] = "ASCII Code: "
    encryptedLabel["text"] = "Encrypted Text: "

    word = inputBox.get()
    inputBox.delete(0, END)

    for letter in word:
        ascii = int(ord(letter))
        encrypted = ascii + 3
        asciiLabel["text"] += str(ascii) + " "
        encryptedLabel["text"] += chr(encrypted)


btn = Button(root, text="Convert To ASCII and Encrypt",
             command=asciiConverter, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

asciiLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
encryptedLabel.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
