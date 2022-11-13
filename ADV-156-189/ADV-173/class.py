class Parent:
    def getMenu(dish):
        if dish == "burger":
            print("You can add the following toppings:")
            print("More Cheese | More Jalapeno")
        elif dish == "icedAmericano":
            print("You can add the following toppings:")
            print("Chocolate flavor | Caramel flavor")

    def finalBill(dish, addon):
        if dish == "burger" and addon == "cheese":
            print("Your bill is: $5.99")
        elif dish == "burger" and addon == "jalapeno":
            print("Your bill is: $6.99")
        elif dish == "icedAmericano" and addon == "chocolate":
            print("Your bill is: $4.99")
        elif dish == "icedAmericano" and addon == "caramel":
            print("Your bill is: $5.99")


class Child1(Parent):
    def __init__(self, dish):
        self.dish = dish

    def getAddons(self):
        Parent.getMenu(self.dish)


class Child2(Parent):
    def __init__(self, dish, addon):
        self.dish = dish
        self.addon = addon

    def getBill(self):
        Parent.finalBill(self.dish, self.addon)


obj1 = Child1("burger")
obj1.getAddons()
print("\n")
obj2 = Child2("icedAmericano", "caramel")
obj2.getBill()
