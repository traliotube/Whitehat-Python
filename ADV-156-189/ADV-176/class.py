from ast import Import
from tkinter import *
import speedtest

root = Tk()
root.title("Speedtest")
root.config(bg="#dee8f1")
root.geometry('500x300')

label = Label(root, text="Speedtest", font=("lucida sans unicode",
              20, "bold", "italic"), fg="#5d6d7e", bg="#dee8f1")
labelDownload = Label(root, text="Download Speed", font=(
    "segoe print", 18, "bold"), fg="#1e8449", bg="#dee8f1")
labelUpload = Label(root, text="Upload Speed", font=(
    "segoe print", 18, "bold"), fg="#1e8449", bg="#dee8f1")
labelDownloadSpeed = Label(root, font=(
    "Yu gothic light", 14, "bold"), bg="#dee8f1")
labelUploadSpeed = Label(root, font=(
    "Yu gothic light", 14, "bold"), bg="#dee8f1")

label.place(relx=0.5, rely=0.1, anchor=CENTER)
labelDownload.place(relx=0.25, rely=0.5, anchor=CENTER)
labelUpload.place(relx=0.75, rely=0.5, anchor=CENTER)
labelDownloadSpeed.place(relx=0.25, rely=0.6, anchor=CENTER)
labelUploadSpeed.place(relx=0.75, rely=0.6, anchor=CENTER)


def speedCheck():
    sp = speedtest.Speedtest()
    labelDownloadSpeed["text"] = str(
        round(sp.download()/1000000, 2)) + "Megabits/s"
    labelUploadSpeed["text"] = str(
        round(sp.upload()/1000000, 2)) + "Megabits/s"


btn = Button(root, text="Check Speed",
             command=speedCheck, bg="#218796", fg="white")
btn.place(relx=0.5, rely=0.3, anchor=CENTER)


root.mainloop()
