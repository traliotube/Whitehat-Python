from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("Classes")
root.geometry('900x600')

elementDropdown = Combobox(root, state="readonly", values=[
                           "Label", "Dropdown", "Button"])
elementDropdown.pack()


class createElements:
    def newLabel(self):
        label = Label(
            root, text="This label has been created using a class.", fg="red")
        label.pack()

    def newButton(self):
        button = Button(
            root, text="Button", fg="red")
        button.pack(padx=20, pady=10)

    def newDropdown(self):
        dropdown = Combobox(root, state="readonly",
                            values=["Test", "Dropdown"])
        dropdown.pack()

    def checkElement(self):
        global elementDropdown
        selected = elementDropdown.get()
        if (selected == "Label"):
            self.newLabel()
        elif (selected == "Dropdown"):
            self.newDropdown()
        elif (selected == "Button"):
            self.newButton()


obj = createElements()

btn = Button(root, text="Create", command=obj.checkElement())
btn.pack(padx=20, pady=10)

root.mainloop()
