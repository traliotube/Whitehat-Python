from tkinter import *
from tkinter.messagebox import showinfo
from simplecrypt import encrypt, decrypt
from tkinter import filedialog as fd

root = Tk()
root.geometry("400x250")


def startDecryption():
    global fileNameEntry
    global decryptionTextData
    root.destroy()

    decryptionWindow = Tk()
    decryptionWindow.geometry("600x500")

    decryptionTextData = Text(decryptionWindow, height=20, width=72)
    decryptionTextData.place(relx=0.5, rely=0.35, anchor=CENTER)

    btn_open_file = Button(
        decryptionWindow, text="Choose File", font='arial 13', command=viewData)
    btn_open_file.place(relx=0.5, rely=0.8, anchor=CENTER)

    decryptionWindow.mainloop()


def startEncryption():
    global fileNameEntry
    global encryptionTextData
    root.destroy()

    encryptionWindow = Tk()
    encryptionWindow.geometry("600x500")

    file_name_label = Label(
        encryptionWindow, text="File Name: ", font='arial 13')
    file_name_label.place(relx=0.1, rely=0.15, anchor=CENTER)

    fileNameEntry = Entry(encryptionWindow, font='arial 15')
    fileNameEntry.place(relx=0.38, rely=0.15, anchor=CENTER)

    btn_create = Button(encryptionWindow, text="Create",
                        font='arial 13', command=setData)
    btn_create.place(relx=0.75, rely=0.15, anchor=CENTER)

    encryptionTextData = Text(encryptionWindow, height=20, width=72)
    encryptionTextData.place(relx=0.5, rely=0.55, anchor=CENTER)

    encryptionWindow.mainloop()


def setData():
    global fileNameEntry
    global encryptionTextData
    file = open(f"{fileNameEntry.get()}.txt", "w")
    cipherCode = encrypt("Password", encryptionTextData.get(0.0, END)).hex()
    print(cipherCode)
    file.write(cipherCode)
    file.close()
    showinfo("Success", "Encrypted file successfully")


def viewData():
    global decryptionTextData

    textFile = fd.askopenfilename(
        title="Open Encrypted File", filetypes=(("Text Files", "*.txt"),))
    data = open(textFile, 'r').read()
    decryptedText = decrypt("Password", bytes.fromhex(data)).decode("utf-8")
    decryptionTextData.insert(0.0, decryptedText)


heading_label = Label(root, text="Encryption & Decryption",
                      font='arial 18 italic')
heading_label.place(relx=0.5, rely=0.2, anchor=CENTER)

btn_start_encryption = Button(
    root, text="Start Encryption", font='arial 13', command=startEncryption)
btn_start_encryption.place(relx=0.3, rely=0.6, anchor=CENTER)

btn_start_decryption = Button(
    root, text="Start Decryption", font='arial 13',  command=startDecryption)
btn_start_decryption.place(relx=0.7, rely=0.6, anchor=CENTER)

root.mainloop()
