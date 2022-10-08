from tkinter import *
from datetime import datetime
from PIL import ImageTk, Image
from pytz import timezone
import time

root = Tk()
root.title("Time")
root.geometry('800x900')

clockImage = ImageTk.PhotoImage(Image.open("clock.jpg"))

indiaLabel = Label(root, text="India")
indiaClock = Label(root, image=clockImage)
indiaTime = Label(root)

usaLabel = Label(root, text="USA Central")
usaClock = Label(root, image=clockImage)
usaTime = Label(root)

japanLabel = Label(root, text="Japan")
japanClock = Label(root, image=clockImage)
japanTime = Label(root)

ukLabel = Label(root, text="United Kingdom")
ukClock = Label(root, image=clockImage)
ukTime = Label(root)


indiaLabel.place(relx=0.2, rely=0.02, anchor=CENTER)
indiaClock.place(relx=0.2, rely=0.2, anchor=CENTER)
indiaTime.place(relx=0.2, rely=0.4, anchor=CENTER)

usaLabel.place(relx=0.7, rely=0.02, anchor=CENTER)
usaClock.place(relx=0.7, rely=0.2, anchor=CENTER)
usaTime.place(relx=0.7, rely=0.4, anchor=CENTER)

japanLabel.place(relx=0.2, rely=0.5, anchor=CENTER)
japanClock.place(relx=0.2, rely=0.7, anchor=CENTER)
japanTime.place(relx=0.2, rely=0.8, anchor=CENTER)

ukLabel.place(relx=0.7, rely=0.5, anchor=CENTER)
ukClock.place(relx=0.7, rely=0.7, anchor=CENTER)
ukTime.place(relx=0.7, rely=0.8, anchor=CENTER)


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
japan = Time("Asia/Tokyo", japanTime)
uk = Time("Europe/London", ukTime)

indiaBtn = Button(root, text="Show Time", command=india.getTime)
usaBtn = Button(root, text="Show Time", command=usa.getTime)
japanBtn = Button(root, text="Show Time", command=japan.getTime)
ukBtn = Button(root, text="Show Time", command=uk.getTime)
indiaBtn.place(relx=0.2, rely=0.44, anchor=CENTER)
usaBtn.place(relx=0.7, rely=0.44, anchor=CENTER)
japanBtn.place(relx=0.2, rely=0.9, anchor=CENTER)
ukBtn.place(relx=0.7, rely=0.9, anchor=CENTER)

root.mainloop()
