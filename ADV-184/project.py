from tkinter import *
from requests import get
from json import loads

root = Tk()
root.geometry("550x500")
root.configure(bg="#00E0FF")
root.overrideredirect(True)

apiRequest = get(
    "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=5eee1796e76f4f7f9de611c2b4a2aa17")
outputJson = loads(apiRequest.content)

canvas = Canvas(
    root,
    bg="#00E0FF",
    height=500,
    width=550,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    167.0,
    21.0,
    anchor="nw",
    text="BBC News Update",
    fill="#000000",
    font=("Inter Bold", 23 * -1)
)

h1 = canvas.create_text(
    32.0,
    63.0,
    anchor="nw",
    text="Heading 1",
    fill="#FFA800",
    font=("Inter SemiBold", 17 * -1),
    width=500
)

t1 = canvas.create_text(
    32.0,
    94.0,
    anchor="nw",
    text="Text 1",
    fill="#000000",
    font=("Inter", 14 * -1),
    width=500
)

h2 = canvas.create_text(
    32.0,
    143.0,
    anchor="nw",
    text="Heading 2",
    fill="#FFA800",
    font=("Inter SemiBold", 17 * -1),
    width=500
)

t2 = canvas.create_text(
    32.0,
    174.0,
    anchor="nw",
    text="Text 2",
    fill="#000000",
    font=("Inter", 14 * -1),
    width=500
)

h3 = canvas.create_text(
    32.0,
    225.0,
    anchor="nw",
    text="Heading 3",
    fill="#FFA800",
    font=("Inter SemiBold", 17 * -1),
    width=500
)

t3 = canvas.create_text(
    32.0,
    254.0,
    anchor="nw",
    text="Text 3",
    fill="#000000",
    font=("Inter", 14 * -1),
    width=500
)

h4 = canvas.create_text(
    32.0,
    305.0,
    anchor="nw",
    text="Heading 4",
    fill="#FFA800",
    font=("Inter SemiBold", 17 * -1),
    width=500
)

t4 = canvas.create_text(
    32.0,
    334.0,
    anchor="nw",
    text="Text 4",
    fill="#000000",
    font=("Inter", 14 * -1),
    width=500
)

h5 = canvas.create_text(
    40.0,
    385.0,
    anchor="nw",
    text="Heading 5",
    fill="#FFA800",
    font=("Inter SemiBold", 17 * -1),
    width=500
)

t5 = canvas.create_text(
    40.0,
    416.0,
    anchor="nw",
    text="Text 5",
    fill="#000000",
    font=("Inter", 14 * -1),
    width=500
)

headings = [h1, h2, h3, h4, h5]
text = [t1, t2, t3, t4, t5]
for i in range(0, 5):
    canvas.itemconfig(headings[i], text=outputJson["articles"][i]["title"])
    canvas.itemconfig(text[i], text=outputJson["articles"][i]["description"])
root.mainloop()
