from tkinter import *

root = Tk()
root.title("Polymorphism")
root.geometry('400x400')

percentageGrade3 = Label(root, text="")
percentageGrade5 = Label(root, text="")
percentageGrade10 = Label(root, text="")


class grade3():
    def __init__(self, sub1, sub2):
        self.sub1 = sub1
        self.sub2 = sub2
        self.total = sub1 + sub2

    def percentage(self):
        percentageGrade3["text"] = str(round((self.total * 100) / 200)) + "%"


class grade5():
    def __init__(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.total = sub1 + sub2 + sub3

    def percentage(self):
        percentageGrade5["text"] = str(round((self.total * 100) / 300)) + "%"


class grade10():
    def __init__(self, sub1, sub2, sub3, sub4):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.sub4 = sub4
        self.total = sub1 + sub2 + sub3 + sub4

    def percentage(self):
        percentageGrade10["text"] = str(round((self.total * 100) / 400)) + "%"


objGrade3 = grade3(82, 93)
objGrade5 = grade5(13, 1, 72)
objGrade10 = grade10(62, 74, 77, 4)

btnGrade3 = Button(root, text="Grade 3", command=objGrade3.percentage)
btnGrade5 = Button(root, text="Grade 5", command=objGrade5.percentage)
btnGrade10 = Button(root, text="Grade 10", command=objGrade10.percentage)

btnGrade3.pack()
percentageGrade3.pack()
btnGrade5.pack()
percentageGrade5.pack()
btnGrade10.pack()
percentageGrade10.pack()

root.mainloop()
