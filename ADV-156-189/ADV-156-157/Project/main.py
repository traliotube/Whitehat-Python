from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Endless Pokemon Game")
root.geometry('600x600')
root.configure(bg="gold")

img = ImageTk.PhotoImage(Image.open("img/button.jpg"))

abra = ImageTk.PhotoImage(Image.open("img/abra.jpg"))
bulbasaur = ImageTk.PhotoImage(Image.open(
    "img/bulbasour.jpg"))
charmander = ImageTk.PhotoImage(Image.open(
    "img/charmender.jpg"))
lyvasour = ImageTk.PhotoImage(Image.open(
    "img/Iyvasour.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open(
    "img/jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("img/kadabra.jpg"))
meowth = ImageTk.PhotoImage(Image.open("img/meowth.jpg"))
nidoking = ImageTk.PhotoImage(Image.open(
    "img/nidoking.jpg"))
paras = ImageTk.PhotoImage(Image.open("img/paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("img/persion.jpg"))
pikachu = ImageTk.PhotoImage(Image.open("img/pikachu.jpg"))
ratata = ImageTk.PhotoImage(Image.open("img/ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open(
    "img/squirtle.jpg"))

list = [abra, bulbasaur, charmander, lyvasour, jigglypuff, kadabra,
        meowth, nidoking, paras, persion, pikachu, ratata, squirtle]
power = [30, 60, 50, 100, 70, 70, 60, 90, 40, 70, 200, 40, 50]

player1 = Label(root, text="Player 1", bg="red", fg="white")
player1.place(relx=0.1, rely=0.2, anchor=CENTER)

player1ScoreLabel = Label(root, text="0", bg="red", fg="white")
player1ScoreLabel.place(relx=0.1, rely=0.3, anchor=CENTER)


player2 = Label(root, text="Player 2", bg="red", fg="white")
player2.place(relx=0.9, rely=0.2, anchor=CENTER)

player2ScoreLabel = Label(root, text="0", bg="red", fg="white")
player2ScoreLabel.place(relx=0.9, rely=0.3, anchor=CENTER)

cardLabel = Label(root, fg="orange",
                  bg="skyblue", font=("Arial", 20))
cardLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

player1Score = 0


def player1():
    global player1Score
    randomPokemon = list[random.randint(0, len(list)-1)]
    cardLabel["image"] = randomPokemon
    player1Score += power[list.index(randomPokemon)]
    player1ScoreLabel["text"] = player1Score


player1Dice = Button(root, image=img, command=player1)
player1Dice.place(relx=0.1, rely=0.5, anchor=CENTER)

player2Score = 0


def player2():
    global player2Score
    randomPokemon = list[random.randint(0, len(list)-1)]
    cardLabel["image"] = randomPokemon
    player2Score += power[list.index(randomPokemon)]
    player2ScoreLabel["text"] = player2Score


player2Dice = Button(root, image=img, command=player2)
player2Dice.place(relx=0.9, rely=0.5, anchor=CENTER)

root.mainloop()
