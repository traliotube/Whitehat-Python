from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.title("Classes")
root.geometry('900x600')


class createElements:
    def new(self):
        label = Label(
            root, text="This label has been created using a class.", fg="red")
        button = Button(root, text="Show Info", command=self.message)
        label.pack()
        button.pack(padx=20, pady=10)

    def message(self):
        showinfo("Classes", "This message box has been created using a class.")


obj = createElements()

btn = Button(root, text="Create a label and a button", command=obj.new)
btn.pack(padx=20, pady=10)

root.mainloop()
