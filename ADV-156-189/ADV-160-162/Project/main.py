import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
from PIL import ImageTk, Image

root = Tk()
root.title("Notepad")
root.minsize(700, 650)
root.maxsize(700, 650)

fileOpenPath = ""
openImg = ImageTk.PhotoImage(Image.open("img/open.png"))
saveImg = ImageTk.PhotoImage(Image.open("img/save.png"))
runImg = ImageTk.PhotoImage(Image.open("img/play.png"))

fileNameLabel = Label(root, text="File Name")
fileNameInput = Entry(root)
textArea = Text(root, height=35, width=75)


def openFile():
    global fileOpenPath
    fileOpenPath = filedialog.askopenfilename(
        title="Open Text File", filetypes=(("HTML Code", "*.html"),))
    print(fileOpenPath)
    baseFileName = os.path.basename(fileOpenPath)
    fileNameInput.insert(0, fileOpenPath)
    root.title(baseFileName + " - Notepad")
    file = open(fileOpenPath, "r")
    fileData = file.read()
    textArea.insert(1.0, fileData)
    file.close()


def save():
    global fileOpenPath
    fileOpenPath = fileNameInput.get()
    if fileOpenPath == "":
        messagebox.showerror("Error", "File Name is Empty")
    else:
        file = open(fileOpenPath, "w")
        data = textArea.get(1.0, END)
        print(data)
        file.write(data)
        messagebox.showinfo("Success", "File Saved")


def run():
    global fileOpenPath
    webbrowser.open("file://" + fileOpenPath)


openBtn = Button(root, image=openImg,
                 command=openFile, borderwidth=0)
saveBtn = Button(root, image=saveImg,
                 command=save, borderwidth=0)
runBtn = Button(root, image=runImg,
                command=run, borderwidth=0)


fileNameLabel.place(relx=0.28, rely=0.03, anchor=CENTER)
fileNameInput.place(relx=0.46, rely=0.03, anchor=CENTER)
textArea.place(relx=0.49, rely=0.55, anchor=CENTER)
openBtn.place(relx=0.05, rely=0.03, anchor=CENTER)
saveBtn.place(relx=0.11, rely=0.03, anchor=CENTER)
runBtn.place(relx=0.17, rely=0.03, anchor=CENTER)

root.mainloop()
