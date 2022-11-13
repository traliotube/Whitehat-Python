from tkinter import *
import random

root = Tk()
root.title("Color Guesser")
root.geometry('800x600')
root.config(bg="white")

label = Label(root, font=("Helvetica", 80), bg="white")
labelScore = Label(root, text="Score", font=("Helvetica", 30), bg="white")
input = Entry(root)


class Game():
    def __init__(self):
        self.__score = 0
        self.__color = 0

    def updateGame(self):
        self.colors = ["red", "blue", "green", "yellow", "orange",
                       "purple", "pink", "black", "white", "brown"]
        self.__color = random.choice(self.colors)
        label["fg"] = self.__color
        label["text"] = random.choice(self.colors)

    def __updateScore(self):
        if self.__color == input.get():
            self.__score += 1
            labelScore["text"] = "Score: " + str(self.__score)
            input.delete(0, END)

    def check(self):
        self.__updateScore()


obj = Game()

checkBtn = Button(root, text="Check", command=obj.check,
                  bg="brown2", fg="white", relief=FLAT, padx=5, pady=1, font=("Helvetica", 20))
startBtn = Button(root, text="Start", command=obj.updateGame,
                  bg="dark green", fg="white", relief=FLAT, padx=5, pady=1, font=("Helvetica", 20))

label.place(relx=0.5, rely=0.4, anchor=CENTER)
labelScore.place(relx=0.1, rely=0.05, anchor=CENTER)
input.place(relx=0.5, rely=0.6, anchor=CENTER)
checkBtn.place(relx=0.3, rely=0.7, anchor=CENTER)
startBtn.place(relx=0.7, rely=0.7, anchor=CENTER)

root.mainloop()
