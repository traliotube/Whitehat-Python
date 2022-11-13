from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Endless Dice Game")
root.geometry('600x400')
root.configure(bg="yellow2")

img = ImageTk.PhotoImage(Image.open("dice.png"))

player1 = Label(root, text="Player 1", bg="royal blue", fg="white")
player1.place(relx=0.1, rely=0.2, anchor=CENTER)

player1ScoreLabel = Label(root, text="0", bg="royal blue", fg="white")
player1ScoreLabel.place(relx=0.1, rely=0.3, anchor=CENTER)


player2 = Label(root, text="Player 2", bg="royal blue", fg="white")
player2.place(relx=0.9, rely=0.2, anchor=CENTER)

player2ScoreLabel = Label(root, text="0", bg="royal blue", fg="white")
player2ScoreLabel.place(relx=0.9, rely=0.3, anchor=CENTER)

diceLabel = Label(root, text="", bg="chocolate1", fg="white")
diceLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

player1Score = 0


def player1():
    global player1Score
    randomNumber = random.randint(1, 6)
    player1Score += randomNumber
    player1ScoreLabel["text"] = player1Score
    diceLabel["text"] = f"Player 1 Dice is a {randomNumber}!"


player1Dice = Button(root, image=img, command=player1)
player1Dice.place(relx=0.1, rely=0.5, anchor=CENTER)

player2Score = 0


def player2():
    global player2Score
    randomNumber = random.randint(1, 6)
    player2Score += randomNumber
    player2ScoreLabel["text"] = player2Score
    diceLabel["text"] = f"Player 2 Dice is a {randomNumber}!"


player2Dice = Button(root, image=img, command=player2)
player2Dice.place(relx=0.9, rely=0.5, anchor=CENTER)

root.mainloop()
