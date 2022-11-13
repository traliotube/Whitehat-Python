from tkinter import messagebox, Tk

root = Tk()
root.title("Key and Index Error")
root.geometry('400x400')

list = ["Micky Mouse", "Else", "Anna", "Donald Duck"]
dict = {
    "name": "Shinchan",
    "age": "5",
}

try:
    print(list[5])
except IndexError:
    messagebox.showerror("IndexError", "List index out of range")

try:
    print(dict["test"])
except KeyError:
    messagebox.showerror("KeyError", "Key not found")

root.mainloop()
