from tkinter import *

root = Tk()
root.title("ASCII")
root.geometry('300x300')

inputBox = Entry(root)
inputBox.place(relx=0.5, rely=0.2, anchor=CENTER)

label = Label(root, text="ASCII Code: ", bg = "lightyellow", fg = "black")

def asciiConverter(): 
    label["text"] = "ASCII Code: " 
    word = inputBox.get()
    
    for letter in word:
        label["text"] += str(ord(letter)) + " "

btn = Button(root, text = "Convert To ASCII", command=asciiConverter, bg = "gold", fg = "black")
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()