from tkinter import *
import time

root = Tk()
root.title("ADV-146 Fibonacci Programming")
root.geometry('600x400')

btn = Button(text="Create Fibonacci Series")
btn.pack()

labelSeries = Label(root, text="Fibonacci Series: ")
labelFlower = Label(root)
labelSpiral = Label(root)

labelSeries.pack()
labelFlower.pack()
labelSpiral.pack()


firstNo = 0
secondNo = 1
sum = 0


def loop(counter=0):
    if counter <= 10:
        global firstNo, secondNo, sum
        labelSeries["text"] += f"{str(sum)} "
        firstNo = secondNo
        secondNo = sum
        sum = firstNo + secondNo
        root.after(500, loop, counter+1)
    labelFlower.config(text="Flower is fully bloomed!")
    labelSpiral.config(
        text=f"Spirals in the right direction are {str(firstNo)} and spirals in the left direction are {str(secondNo)}. Total no of spirals are {str(sum)}")


btn.config(command=loop)

root.mainloop()
