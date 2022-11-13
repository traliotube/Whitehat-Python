from tkinter import *
from tkinter import filedialog as fd
import hashlib

root = Tk()
root.geometry("250x190")


def apply_md5():
    textFile = fd.askopenfilename(
        title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    readFile = open(textFile, 'r')
    data = readFile.read()
    result = hashlib.md5(data.encode()).hexdigest()
    newFile = open("ADV-185/Project/md5.txt", "w").write(result)


def apply_sha256():
    textFile = fd.askopenfilename(
        title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    readFile = open(textFile, 'r')
    data = readFile.read()
    result = hashlib.sha256(data.encode()).hexdigest()
    newFile = open("ADV-185/Project/sha256.txt", "w").write(result)


btn = Button(root, text="Apply MD5", command=apply_md5)
btn.place(relx=0.3, rely=0.5, anchor=CENTER)
btn1 = Button(root, text="Apply SHA256", command=apply_sha256)
btn1.place(relx=0.7, rely=0.5, anchor=CENTER)
root.mainloop()
