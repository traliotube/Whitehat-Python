from tkinter import *

root = Tk()
root.title("ADV-146 Fibonacci Programming")
root.configure(background="#ffbe28")
root.geometry('600x400')

btn = Button(root, text="Create Fibonacci Series", fg="white", bg="#0597ff")
btn.pack()


labelSeries = Label(root, text="Fibonacci Series: ")
labelSum = Label(root, text="Fibonacci Sum: ")

labelSeries.pack()
labelSum.pack()


firstNo = 0
secondNo = 1
sum = 0
totalSum = 0


def loop(counter=0):
    if counter <= 10:
        global firstNo, secondNo, sum, totalSum
        labelSeries["text"] += f"{str(sum)} "
        firstNo = secondNo
        secondNo = sum
        sum = firstNo + secondNo
        labelSum.config(text="Fibonacci Sum: " + str(totalSum))
        totalSum += sum
        root.after(500, loop, counter+1)
    print(labelSeries["text"])


btn.config(command=loop)

root.mainloop()
