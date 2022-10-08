from tkinter import *
from datetime import datetime
from PIL import ImageTk, Image
from pytz import timezone
import time

root = Tk()
root.title("Time")
root.geometry('600x450')

clockImage = ImageTk.PhotoImage(Image.open("clock.jpg"))

indiaLabel = Label(root, text="India")
indiaClock = Label(root, image=clockImage)
indiaTime = Label(root)

usaLabel = Label(root, text="USA Central")
usaClock = Label(root, image=clockImage)
usaTime = Label(root)

indiaLabel.place(relx=0.2, rely=0.05, anchor=CENTER)
indiaClock.place(relx=0.2, rely=0.35, anchor=CENTER)
indiaTime.place(relx=0.2, rely=0.65, anchor=CENTER)

usaLabel.place(relx=0.7, rely=0.05, anchor=CENTER)
usaClock.place(relx=0.7, rely=0.35, anchor=CENTER)
usaTime.place(relx=0.7, rely=0.65, anchor=CENTER)


class Time():
    def __init__(self, timezone, label):
        self.timezone = timezone
        self.label = label

    def getTime(self):
        self.label["text"] = datetime.now(
            timezone(self.timezone)).strftime("%H:%M:%S")
        self.label.after(1, self.getTime)


india = Time("Asia/Kolkata", indiaTime)
usa = Time("US/Central", usaTime)

indiaBtn = Button(root, text="Show Time", command=india.getTime)
usaBtn = Button(root, text="Show Time", command=usa.getTime)
indiaBtn.place(relx=0.2, rely=0.8, anchor=CENTER)
usaBtn.place(relx=0.7, rely=0.8, anchor=CENTER)

root.mainloop()
