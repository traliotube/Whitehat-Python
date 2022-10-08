import tkinter as tk

root = tk.Tk()
root.title("ADV-145")
root.geometry('400x400')

resultLabel = tk.Label(root)


def add():
    result = 100+200
    resultLabel["text"] = f"Result of 100+200 is {result}"


button = tk.Button(text="Add 100+200", command=add)


button.pack()
resultLabel.pack()

root.mainloop()
