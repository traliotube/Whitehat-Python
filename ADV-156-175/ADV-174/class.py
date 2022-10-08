from audioop import add
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox

root = Tk()
root.title("Rdonalds")
root.geometry('900x500')

burgerImg = ImageTk.PhotoImage(Image.open("burger.png"))

labelImg = Label(root, image=burgerImg,)
labelHeading = Label(root, text="Rdonalds", font=(
    "times", 40, "bold"), fg="orange")
labelSelectDish = Label(root, text="Select the Dish", font=("times", 15))
labelSelectAddons = Label(root, text="Select the Addons", font=("times", 15))
finalAmount = Label(root, font=("times", 15, "bold"))

dishes = ["burger", "icedAmericano"]
dishDropdown = Combobox(
    root, values=dishes, state="readonly")
toppings = []
addonsDropdown = Combobox(root, values=toppings, state="readonly")


labelImg.place(relx=0.7, rely=0.5, anchor=CENTER)
labelHeading.place(relx=0.12, rely=0.1, anchor=CENTER)
labelSelectDish.place(relx=0.06, rely=0.2, anchor=CENTER)
dishDropdown.place(relx=0.25, rely=0.2)
labelSelectAddons.place(relx=0.08, rely=0.5, anchor=CENTER)
addonsDropdown.place(relx=0.25, rely=0.5)
finalAmount.place(relx=0.2, rely=0.75, anchor=CENTER)


class Parent:
    def getMenu(dish):
        global addonsDropdown
        if dish == "burger":
            toppings = ["More Cheese", "More Jalapeno"]
            addonsDropdown["values"] = toppings
        elif dish == "icedAmericano":
            toppings = ["Chocolate flavor", "Caramel flavor"]
            addonsDropdown["values"] = toppings

    def finalBill(dish, addon):
        if dish == "burger" and addon == "cheese":
            finalAmount["text"] = "Your bill is: $5.99"
        elif dish == "burger" and addon == "jalapeno":
            finalAmount["text"] = "Your bill is: $6.99"
        elif dish == "icedAmericano" and addon == "chocolate":
            finalAmount["text"] = "Your bill is: $4.99"
        elif dish == "icedAmericano" and addon == "caramel":
            finalAmount["text"] = "Your bill is: $5.99"


class Child1(Parent):
    def __init__(self, dish):
        self.dish = dish

    def getAddons(self):
        dish = dishDropdown.get()
        Parent.getMenu(self.dish)


class Child2(Parent):
    def __init__(self, dish, addons):
        self.dish = dish
        self.addon = addons

    def getBill(self):
        dish = dishDropdown.get()
        addons = addonsDropdown.get()
        Parent.finalBill(dish, addons)


obj1 = Child1(dishDropdown.get())
obj1.getAddons()
obj2 = Child2(dishDropdown.get(), addonsDropdown.get())
obj2.getBill()

btnAddon = Button(root, text="Show Addons",
                  command=obj1.getAddons(), bg="blue", fg="white")
btnBill = Button(root, text="Show Final Amount",
                 command=obj2.getBill(), bg="blue", fg="white")

btnAddon.place(relx=0.06, rely=0.3, anchor=CENTER)
btnBill.place(relx=0.04, rely=0.6, anchor=CENTER)
root.mainloop()
