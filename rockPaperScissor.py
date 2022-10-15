
import random

class RockPaperScissor():

    gamer = ["computer", "player", "tie"]
    choiceList = ["r", "p", "s"]  # r for rock, p for paper, s for sissor

    def computerChoice(self):   # random choice by computer
        return random.choice(self.choiceList)

    @staticmethod
    def PlayerChoice():  # choice by user/player/human
        playerInput = input("\nPlease enter r for rock, or p for paper, or s for scissors or q for quit: " )
        return playerInput


    @staticmethod
    def pointAdd(currentPoint):
        currentPoint += 1  # addition of point for winning a round
        return currentPoint

    def winningPoint(self, currentPoint):
        pointAchieved = False
        if currentPoint == 5:
            pointAchieved = True  # if either player or computer achieve 5 points, wins the game
        return pointAchieved

    def setWinner(self, playerChoice, computerChoice):
        winner = ''

        if playerChoice==computerChoice:
            winner=self.gamer[2]   # computer and user both have same choice, so nobody gets point at this round

        elif playerChoice == 'r':
            if computerChoice =='p':
               winner=self.gamer[0]   # computer wins this round as per given condition, so will get 1 point
            else : 
               winner=self.gamer[1]   # player wins this round as per given condition, so will get 1 point
        elif playerChoice =='p':
            if computerChoice =='s':
               winner=self.gamer[0]   # computer wins this round as per given condition, so will get 1 point
            else:
               winner=self.gamer[1]   # computer wins this round as per given condition, so will get 1 point
        elif playerChoice =='s':
            if computerChoice =='p':
               winner=self.gamer[1]   # computer wins this round as per given condition, so will get 1 point
            else:
               winner=self.gamer[0]   # computer wins this round as per given condition, so will get 1 point

        return winner

    def start(self):

        playerPoint = computerPoint =roundNumber = 0

        while playerPoint != 5 or computerPoint != 5:

            playerChoice = self.PlayerChoice()  # input player choice

            if playerChoice in self.choiceList:  # checking if choice is valid i.e, rock paper or scissor

                roundNumber += 1
                print("Round:", roundNumber)

                computerChoice = self.computerChoice()
                print("Computer chose:", computerChoice)

                winner = self.setWinner(playerChoice, computerChoice)

                if winner == 'player':
                    playerPoint = self.pointAdd(playerPoint)  # adding score to winner
                    print("Congratz! You have won this round !")
                    print("Your point is:", playerPoint)
                    print("Computer's point is:", computerPoint)

                elif winner == 'computer':
                    computerPoint = self.pointAdd(computerPoint)
                    print("Computer have won this round")
                    print("Your point is:", playerPoint)
                    print("Computer's point is:", computerPoint)

                else:  
                    print("Tie!")  # tie

                if self.winningPoint(playerPoint) or self.winningPoint(computerPoint): # if anyone achieved winning point

                    if self.winningPoint(playerPoint):
                        print("\n\nCongratz! you won the match !!")
                    else:
                        print("\n\nComputer won the Game ! ")  

                    print("\nNumber of total rounds played: {}\n".format(roundNumber))

                    break


            elif playerChoice == 'q':  # player may quit the game anytime
                break
            else:  # if invalid user input
                print("Invalid input! Please type r, p, s or q as your input.")

    def replay(self):   # player may quit or restart the game after winner is determined

        quitGame = False

        while not quitGame:  # play again until user quit the game
            self.start()

            gameContinuation = input("\nTo exit the game enter q or to restart enter rs: ").lower().strip()

            if gameContinuation == "q":
                quitGame = True
            elif gameContinuation == "rs":
                quitGame = False
            else:
                print("Invalid input! Please enter q or rs")


def main():

    game = RockPaperScissor()
    game.replay()


if __name__ == "__main__":
    main()
