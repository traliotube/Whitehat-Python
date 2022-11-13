from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Fever Report")
root.geometry('600x600')

q1Value = StringVar(value="0")
q1 = Label(root, text="Do you have headache and sore throat?")
q1RadioBtn1 = Radiobutton(root, text="Yes", variable=q1Value, value="Yes")
q1RadioBtn2 = Radiobutton(root, text="No", variable=q1Value, value="No")

q2Value = StringVar(value="0")
q2 = Label(root, text="Is your body temperature high?")
q2RadioBtn1 = Radiobutton(root, text="Yes", variable=q2Value, value="Yes")
q2RadioBtn2 = Radiobutton(root, text="No", variable=q2Value, value="No")

q3Value = StringVar(value="0")
q3 = Label(root, text="Are there any symptoms of any eye redness?")
q3RadioBtn1 = Radiobutton(root, text="Yes", variable=q3Value, value="Yes")
q3RadioBtn2 = Radiobutton(root, text="No", variable=q3Value, value="No")


def feverScore():
    score = 0
    if q1Value.get() == "Yes":
        score += 20
    if q2Value.get() == "Yes":
        score += 20
    if q3Value.get() == "Yes":
        score += 20

    if score <= 20:
        messagebox.showinfo("Report", "No need to visit the doctor")
    elif score > 20 and score <= 40:
        messagebox.showwarning("Report", "You better visit the doctor")
    else:
        messagebox.showerror("Report", "You must visit the doctor")


btn = Button(root, text="Submit", command=feverScore)

q1.pack()
q1RadioBtn1.pack()
q1RadioBtn2.pack()

q2.pack()
q2RadioBtn1.pack()
q2RadioBtn2.pack()

q3.pack()
q3RadioBtn1.pack()
q3RadioBtn2.pack()

btn.pack()

root.mainloop()
