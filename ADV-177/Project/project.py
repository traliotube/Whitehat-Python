from pathlib import Path
from tkinter import *
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./img")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = Tk()
root.geometry("700x700")
root.configure(bg="#FFFFFF")

canvas = Canvas(
    root,
    bg="#FFFFFF",
    height=700,
    width=700,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    406.0,
    114.0,
    image=entry_image_1
)
nameInput = Entry(
    bd=0,
    bg="#E4E4E4",
    highlightthickness=0
)
nameInput.place(
    x=250.0,
    y=95.0,
    width=312.0,
    height=36.0
)

canvas.create_text(
    33.0,
    96.0,
    anchor="nw",
    text="Name",
    fill="#000000",
    font=("Inter", 30 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    406.0,
    181.0,
    image=entry_image_2
)
passwordInput = Entry(
    bd=0,
    bg="#E4E4E4",
    highlightthickness=0
)
passwordInput.place(
    x=250.0,
    y=162.0,
    width=312.0,
    height=36.0
)

canvas.create_text(
    33.0,
    163.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 30 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_3_img = canvas.create_image(
    406.0,
    249.0,
    image=entry_image_3
)
captchaInput = Entry(
    bd=0,
    bg="#E4E4E4",
    highlightthickness=0
)
captchaInput.place(
    x=250.0,
    y=230.0,
    width=312.0,
    height=36.0
)

canvas.create_text(
    33.0,
    231.0,
    anchor="nw",
    text="Captcha",
    fill="#000000",
    font=("Inter", 30 * -1)
)

captchaLabel = canvas.create_text(
    105.0,
    497.0,
    anchor="nw",
    text="Captcha:",
    fill="#000000",
    font=("Inter", 25 * -1)
)

passwordLabel = canvas.create_text(
    105.0,
    454.0,
    anchor="nw",
    text="Password",
    fill="#000000",
    font=("Inter", 25 * -1)
)

nameLabel = canvas.create_text(
    105.0,
    411.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Inter", 25 * -1)
)


class UserDB():
    def __init__(self):
        self.__name = "Sample"
        self.__password = "password123"
        self.captcha = "ABC123"

    def showUser(self):
        canvas.itemconfig(nameLabel, text=f"Name: {self.__name}")
        canvas.itemconfig(passwordLabel, text=f"Password: {self.__password}")
        canvas.itemconfig(captchaLabel, text=f"Captcha: {self.captcha}")


obj = UserDB()


def addUser():
    global obj
    obj.__name = nameInput.get()
    obj.__password = passwordInput.get()
    obj.captcha = captchaInput.get()
    print("Details Updated")


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
showBtn = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: obj.showUser(),
    relief="flat"
)
showBtn.place(
    x=365.0,
    y=327.0,
    width=269.0,
    height=47.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
updateBtn = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: addUser(),
    relief="flat"
)
updateBtn.place(
    x=34.0,
    y=327.0,
    width=352.0,
    height=47.0
)


root.resizable(False, False)
root.mainloop()
