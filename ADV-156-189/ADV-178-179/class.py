from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Combobox

root = Tk()
root.title("Juice Dispenser")
root.geometry('800x600')
root.config(bg="orange2")

juiceImg = ImageTk.PhotoImage(Image.open("img/logo.png"))
apple = ImageTk.PhotoImage(Image.open("img/apple_img.png"))
mango = ImageTk.PhotoImage(Image.open("img/mango_img.png"))
orange = ImageTk.PhotoImage(Image.open("img/orange.png"))

labelHeading = Label(root, text="Juice Dispenser",
                     font=("Sylfaen", 18, "bold", "italic"), bg="orange")
juice = Label(root, image=juiceImg, bg="orange")
fruitImg = Label(root, bg="orange2")
labelName = Label(root, text="Select Fruit", font=(
    "Bahnschrift Light", 15), bg="orange2")
labelQuantity = Label(root, text="Enter Quantity", font=(
    "Bahnschrift Light", 15), bg="orange2")

fruitList = ["Apple", "Mango", "Orange"]
fruitDropdown = Combobox(root, state="readonly",
                         values=fruitList, justify="right")
inputQuantity = Entry(root)
inputQuantity.place(relx=0.95, rely=0.4, anchor=E)

labelShowAmnt = Label(root, font=("Bahnschrift Light", 12), bg="orange2")
labelShowQuantity = Label(root, font=("Bahnschrift Light", 12), bg="orange2")

labelShowQuantity.place(relx=0.95, rely=0.8, anchor=E)
labelShowAmnt.place(relx=0.95, rely=0.7, anchor=E)
labelQuantity.place(relx=0.96, rely=0.35, anchor=E)
fruitDropdown.place(relx=0.95, rely=0.25, anchor=E)
labelName.place(relx=0.96, rely=0.2, anchor=E)
juice.place(relx=0.2, rely=0.4, anchor=CENTER)
labelHeading.place(relx=0.05, rely=0.1, anchor=W)
fruitImg.place(relx=0.75, rely=0.8, anchor=CENTER)


class Juice():
    def __init__(self, fruit, quantity):
        self.fruit = fruit
        self.quantity = quantity
        self.__price = 250

    def __calculatePrice(self):
        labelShowAmnt["text"] = f"You have to Pay ₹{str(self.quantity * self.__price)}"
        if self.fruit == "Apple":
            calorie = self.quantity * 52
            fruitImg["image"] = apple
        elif self.fruit == "Mango":
            calorie = self.quantity * 60
            fruitImg["image"] = mango
        elif self.fruit == "Orange":
            calorie = self.quantity * 47
            fruitImg["image"] = orange
        labelShowQuantity["text"] = (
            f"x {str(self.quantity)} = {str(calorie)}cal")

    def getCost(self):
        self.__calculatePrice()


def orderJuice():
    fruit = fruitDropdown.get()
    quantity = int(inputQuantity.get())
    obj = Juice(fruit, quantity)
    obj.getCost()


btn = Button(root, text="Order Juice", command=orderJuice)
btn.place(relx=0.95, rely=0.5, anchor=E)

root.mainloop()
