class Main():
    def __init__(self):
        self.score = 1
        self.__pScore = 1

    def updateScore(self):
        self.__pScore += 1
        self.score += 1
        print(f"Score: {self.score}, pScore: {self.__pScore}")


obj = Main()
obj.score = 5
obj.__pScore = 5
obj.updateScore()
obj.updateScore()
