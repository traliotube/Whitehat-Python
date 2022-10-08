from tkinter import *

root = Tk()
root.title("Sales Application")
root.geometry('600x600')
root.configure(bg="skyblue")

months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
profits = (218983, 207077, 306519, 135127, 477549, 262648,
           397945, 475812, 197306, 154309, 481541, 419896)

monthLabel = Label(root, text=months)
profitsLabel = Label(root, text=profits)
maxProfit = Label(root)
minProfit = Label(root)


def minProfitCalc():
    minProfitNumber = min(profits)
    minProfitIndex = profits.index(minProfitNumber)
    minProfixMonth = months[minProfitIndex]
    minProfit["text"] = f"The month with the lowest profit is {minProfixMonth} with {minProfitNumber}. The index is {minProfitIndex}."


def maxProfitCalc():
    maxProfitNumber = max(profits)
    maxProfitIndex = profits.index(maxProfitNumber)
    maxProfixMonth = months[maxProfitIndex]
    maxProfit["text"] = f"The month with the highest profit is {maxProfixMonth} with {maxProfitNumber}. The index is {maxProfitIndex}."


maxBtn = Button(root, text="Show Max Profit", command=maxProfitCalc)
minBtn = Button(root, text="Show Min Profit", command=minProfitCalc)

monthLabel.place(relx=0.5, rely=0.2, anchor=CENTER)
profitsLabel.place(relx=0.5, rely=0.3, anchor=CENTER)
maxBtn.place(relx=0.5, rely=0.4, anchor=CENTER)
maxProfit.place(relx=0.5, rely=0.5, anchor=CENTER)
minBtn.place(relx=0.5, rely=0.6, anchor=CENTER)
minProfit.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()
