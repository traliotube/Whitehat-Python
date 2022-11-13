from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Detecting Cardiovascular Symptoms")
root.geometry('600x600')

q1Value = StringVar(value="0")
q1 = Label(
    root, text="Do you experience shortness of breath during routine activities?")
q1RadioBtn1 = Radiobutton(root, text="Yes", variable=q1Value, value="Yes")
q1RadioBtn2 = Radiobutton(root, text="No", variable=q1Value, value="No")

q2Value = StringVar(value="0")
q2 = Label(
    root, text="Do you have swelling in the feet/ankles/legs (shoes feel tighter) or abdomen?")
q2RadioBtn1 = Radiobutton(root, text="Yes", variable=q2Value, value="Yes")
q2RadioBtn2 = Radiobutton(root, text="No", variable=q2Value, value="No")

q3Value = StringVar(value="0")
q3 = Label(
    root, text="Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
q3RadioBtn1 = Radiobutton(root, text="Yes", variable=q3Value, value="Yes")
q3RadioBtn2 = Radiobutton(root, text="No", variable=q3Value, value="No")

q4Value = StringVar(value="0")
q4 = Label(
    root, text="Do you experience shortness of breath while at rest/lying down? ")
q4RadioBtn1 = Radiobutton(root, text="Yes", variable=q4Value, value="Yes")
q4RadioBtn2 = Radiobutton(root, text="No", variable=q4Value, value="No")

q5Value = StringVar(value="0")
q5 = Label(root, text="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?")
q5RadioBtn1 = Radiobutton(root, text="Yes", variable=q5Value, value="Yes")
q5RadioBtn2 = Radiobutton(root, text="No",  variable=q5Value, value="No")


def feverScore():
    score = 0
    if q1Value.get() == "Yes":
        score += 20
    if q2Value.get() == "Yes":
        score += 20
    if q3Value.get() == "Yes":
        score += 20
    if q4Value.get() == "Yes":
        score += 20
    if q5Value.get() == "Yes":
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

q4.pack()
q4RadioBtn1.pack()
q4RadioBtn2.pack()

q5.pack()
q5RadioBtn1.pack()
q5RadioBtn2.pack()

btn.pack()

root.mainloop()
