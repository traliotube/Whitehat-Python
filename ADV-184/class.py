from tkinter import *
from tkinter import ttk
import psutil
from psutil._common import BatteryTime
import time
import datetime

root = Tk()
root.geometry('500x250')
root.config(bg="black")
root.overrideredirect(True)

batteryLife = Label(root, font='arial 15 bold', bg='black', fg="white")
batteryLife.place(relx=0.5, rely=0.5, anchor=CENTER)

style = ttk.Style(root)
style.layout('ProgressBarStyle', [('Horizontal.Progressbar.trough', {'children': [('Horizontal.Progressbar.pbar', {
             'side': 'right', 'sticky': 'ns'})], 'sticky': 'nsew'}), ('Horizontal.Progressbar.label', {'sticky': ''})])

bar = ttk.Progressbar(root, maximum=100, style="ProgressBarStyle")
bar.place(relx=0.5, rely=0.2, anchor=CENTER)


def getBatteryLife():
    battery = psutil.sensors_battery()
    bar["value"] = battery.percent
    style.configure("ProgressBarStyle", text=str(battery.percent)+"%")
    batteryLeft = time.strftime("%H:%M:%S", time.gmtime(battery.secsleft))
    if batteryLeft == BatteryTime.POWER_TIME_UNLIMITED:
        batteryLife["text"] = "Please unplug your laptop\n and run the program again"
    elif batteryLeft == BatteryTime.POWER_TIME_UNKNOWN:
        batteryLife["text"] = "Battery life not detected\n Please run the program again"
    else:
        batteryLife["text"] = "Battery Life: " + str(batteryLeft)
        root.after(1000, getBatteryLife)


getBatteryLife()

root.mainloop()
