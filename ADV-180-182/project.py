from cgitb import text
from msilib.schema import ODBCTranslator
from time import sleep
from tkinter import *
from tkinter.ttk import Combobox
import googletrans

root = Tk()
root.title("Speech Recognizer")
root.geometry('800x500')
root.config(bg="gold2")

labelHeading = Label(root, text="Language Translator",
                     font=("Times", 20, "bold"))
labelInput = Label(root, text="Enter Text:", font=("Courier", 15), bg="gold2")
textinput = Text(root, height=10, width=30)
labelOutput = Label(root, text="Output Text:",
                    font=("Courier", 15), bg="gold2")
textOutput = Text(root, height=10, width=30)
inputLang = StringVar()
outputLang = StringVar()
inputCombo = Combobox(root, values=list(
    googletrans.LANGUAGES.values()), textvariable=inputLang)
outputCombo = Combobox(root, values=list(
    googletrans.LANGUAGES.values()), textvariable=outputLang)

labelHeading.place(relx=0.5, rely=0.1, anchor=CENTER)
labelInput.place(relx=0.1, rely=0.3, anchor=CENTER)
inputCombo.place(relx=0.3, rely=0.3, anchor=CENTER)
textinput.place(relx=0.2, rely=0.5, anchor=CENTER)
labelOutput.place(relx=0.7, rely=0.3, anchor=CENTER)
outputCombo.place(relx=0.9, rely=0.3, anchor=CENTER)
textOutput.place(relx=0.8, rely=0.5, anchor=CENTER)


def translate():
    obj = googletrans.Translator()
    textOutput.delete(1.0, END)
    textOutput.insert(1.0, obj.translate(
        textinput.get(1.0, END), outputCombo.get(), inputCombo.get()).text)


btn = Button(root, text="Translate", command=translate, bg="lightblue")
btn.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
