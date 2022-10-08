from tkinter import *

root = Tk()
root.title("Multidimensional Array")
root.geometry('500x500')

label = Label(root)

array1D = ["John", "James", "Thomson"]
print(array1D)

array2D = [["John", "A+"], ["James", "A"], ["Thomson", "B"]]
print(array2D)

array3D = [[["John", "A+", "Excellent"],
           ["James", "A", "Very Good"], ["Thomson", "B", "Good"]]]
print(array3D)


def reportCard():
    for i in array3D:
        label["text"] += "{} has got Grade {}, he has aso got {} as feedback \n".format(
            i[0], i[1], i[2])


btn = Button(root, text="Show Report cards", command=reportCard)

btn.place(relx=0.5, rely=0.3, anchor=CENTER)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
