from msilib.schema import ComboBox
from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, PhotoImage
from tkinter.ttk import Combobox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./img")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = Tk()

root.geometry("950x700")
root.configure(bg="#FFFFFF")


canvas = Canvas(
    root,
    bg="#FFFFFF",
    height=700,
    width=950,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    33.0,
    572.0,
    anchor="nw",
    text="Start X",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    175.68722534179688,
    585.0,
    image=entry_image_1
)
startXEntry = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
startXEntry.place(
    x=113.37445068359375,
    y=572.0,
    width=124.62554931640625,
    height=24.0
)

canvas.create_text(
    494.0,
    572.0,
    anchor="nw",
    text="End X",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    636.6872253417969,
    585.0,
    image=entry_image_2
)
startYEntry = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
startYEntry.place(
    x=574.3744506835938,
    y=572.0,
    width=124.62554931640625,
    height=24.0
)

canvas.create_text(
    711.0,
    572.0,
    anchor="nw",
    text="End Y\n",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    853.6872253417969,
    585.0,
    image=entry_image_3
)
endYEntry = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
endYEntry.place(
    x=791.3744506835938,
    y=572.0,
    width=124.62554931640625,
    height=24.0
)

canvas.create_text(
    271.0,
    572.0,
    anchor="nw",
    text="Start Y\n",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    413.6872253417969,
    585.0,
    image=entry_image_4
)
endXEntry = Entry(
    bd=0,
    bg="#C4C4C4",
    highlightthickness=0
)
endXEntry.place(
    x=351.37445068359375,
    y=572.0,
    width=124.62554931640625,
    height=24.0
)

canvas.create_text(
    316.0,
    641.0,
    anchor="nw",
    text="Choose Fill Colour:",
    fill="#000000",
    font=("Inter", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    571.6872253417969,
    654.0,
    image=entry_image_5
)

colour = StringVar()

coloursList = ["red", "blue", "green", "orange",
               "purple", "yellow", "pink", "black", "white"]

colourEntry = Combobox(
    background="#C4C4C4",
    values=coloursList,
    textvariable=colour,
    state="readonly"
)

colourEntry.place(
    x=509.37445068359375,
    y=641.0,
    width=124.62554931640625,
    height=24.0
)


def oval(event):
    canvas.create_oval(startXEntry.get(),
                       startYEntry.get(), endXEntry.get(), endYEntry.get(), fill=colourEntry.get())


def rect(event):
    canvas.create_rectangle(startXEntry.get(),
                            startYEntry.get(), endXEntry.get(), endYEntry.get(), fill=colourEntry.get())


def line(event):
    canvas.create_line(startXEntry.get(),
                       startYEntry.get(), endXEntry.get(), endYEntry.get(), fill=colourEntry.get())


root.bind("c", oval)
root.bind("r", rect)
root.bind("l", line)

root.resizable(False, False)
root.mainloop()
