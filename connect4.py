from board import Board

class Connect4():
    
    def __init__(self):
        self.board = Board()

    def start(self):
        while not self.isGameOver():
            self.printBoard()
            self.printTurn()
            col = self.getUserInput()
            self.placeTile(col)
            if self.isGameOver:
                self.printWinner()

    def getUserInput(self):
        userInput = input("Enter column number: ")

        while not userInput.isnumeric() or not self.board.isValidPlacement(int(userInput)):
            print("Invalid column number")
            userInput = input("Enter column number: ")

        return int(userInput)
    
    def printBoard(self):
        self.board.printBoard()
    
    def printTurn(self):
        if self.board.turn:
            print("Player 1's Turn")
        else:
            print("Player 2's Turn")

    def printWinner(self):
        print("Player {} Wins".format(self.board.winner))

    def placeTile(self, col):
        self.board.placeTile(col)

    def isGameOver(self):
        return self.board.isGameOver
    
if __name__ == "__main__":
    game = Connect4()
    game.start()