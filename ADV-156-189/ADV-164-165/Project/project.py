import imghdr
import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.geometry('500x500')
root.configure(bg="lightblue")

imgLabel = Label(root)

filePath = ""


def openImg():
    global filePath
    filePath = filedialog.askopenfilename(
        title="Open Image", filetypes=[("Images", "*.jpg *.gif *.png *.jpeg")])
    print(filePath)
    img = ImageTk.PhotoImage(Image.open(filePath))
    imgLabel["image"] = img
    img.close()


def rotateImg():
    global filePath
    img = ImageTk.PhotoImage(Image.open(filePath).rotate(90))
    imgLabel["image"] = img
    img.close()


openBtn = Button(root, text="Open Image", command=openImg)
rotateBtn = Button(root, text="Rotate Image", command=rotateImg)

openBtn.place(relx=0.5, rely=0.05, anchor=CENTER)
imgLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
rotateBtn.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
