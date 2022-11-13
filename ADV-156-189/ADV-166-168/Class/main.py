from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Canvas Drawing")
root.geometry('600x600')

canvas = Canvas(root, width=590, height=550, bg='white',
                highlightbackground="lightgrey")

brushImg = ImageTk.PhotoImage(Image.open("brush.png"))
artistImgCanvas = canvas.create_image(50, 50, image=brushImg)

colourLabel = Label(root, text="Enter Line Colour:")
inputColour = Entry(root)
inputColour.insert(0, "black")

canvas.pack()
colourLabel.place(relx=0.6, rely=0.95, anchor=CENTER)
inputColour.place(relx=0.8, rely=0.95, anchor=CENTER)


direction = ""
startX = 50
startY = 50
endX = 50
endY = 50


def drawLine(startX, startY, endX, endY):
    fillColour = inputColour.get()
    canvas.create_line(startX, startY, endX, endY, fill=fillColour)


def rightDir(event):
    global startX, startY, endX, endY, direction
    startX = endX
    startY = endY
    endX = endX + 10
    direction = "right"
    drawLine(startX, startY, endX, endY)
    canvas.move(artistImgCanvas, 10, 0)


def leftDir(event):
    global startX, startY, endX, endY, direction
    startX = endX
    startY = endY
    endX = endX - 10
    direction = "right"
    drawLine(startX, startY, endX, endY)
    canvas.move(artistImgCanvas, -10, 0)


def upDir(event):
    global startX, startY, endX, endY, direction
    startX = endX
    startY = endY
    endY = endY - 10
    direction = "right"
    drawLine(startX, startY, endX, endY)
    canvas.move(artistImgCanvas, 0, -10)


def downDir(event):
    global startX, startY, endX, endY, direction
    startX = endX
    startY = endY
    endY = endY + 10
    direction = "right"
    drawLine(startX, startY, endX, endY)
    canvas.move(artistImgCanvas, 0, 10)


root.bind("<Right>", rightDir)
root.bind("<Left>", leftDir)
root.bind("<Up>", upDir)
root.bind("<Down>", downDir)


root.mainloop()
