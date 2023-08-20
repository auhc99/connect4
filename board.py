ROWS = 6
COLS = 7
WIN = 4

class Board:
    
    def __init__(self):
        self.board = [['.' for _ in range(COLS)] for _ in range(ROWS)]
        self.turn = True # use to alternate between turns, true = player 1, false = player 2
        self.isGameOver = False # checks game state of board
        self.winner = None # gets the winner
        self.PLAYER_TO_TILE = {
          True: "O",
          False : 'X'
        }
    
    def isValidPlacement(self, col):
        if col >= COLS:
            return False
        elif self.board[-1][col] != '.':
            return False
        else:
            return True

    def placeTile(self, col):
        row = -1
        
        for i in range(ROWS):
            if self.board[i][col] == '.':
                self.board[i][col] = self.PLAYER_TO_TILE[self.turn]
                row = i
                break

        if self.checkForWin(row, col):
            self.winner = int(self.turn)
            self.isGameOver = True
        else:
            self.turn = not self.turn

    def checkForWin(self, row, col):
        if self.board[row][col] == '.':
            return False
        if self.checkHorizontal(row, col) or self.checkVertical(row, col) or self.checkDiagonal(row, col):
            return True
        return False

    def checkHorizontal(self, row, col):
        tile = self.board[row][col]
        nTiles = 1

        for j in range(col - 1, -1, -1):
            if self.board[row][j] == tile:
                nTiles += 1
                if nTiles == WIN:
                    return True
            else:
                break

        for j in range(col + 1, COLS):
            if self.board[row][j] == tile:
                nTiles += 1
                if nTiles == WIN:
                    return True
            else:
                break

        if nTiles >= WIN:
            return True
        else:
            return False

    def checkVertical(self, row, col):
        tile = self.board[row][col]
        nTiles = 1

        for i in range(row - 1, -1, -1):
            if self.board[i][col] == tile:
                nTiles += 1
                if nTiles == WIN:
                    return True
            else:
                break

        for i in range(row + 1, ROWS):
            if self.board[i][col] == tile:
                nTiles += 1
                if nTiles == WIN:
                    return True
            else:
                break

        if nTiles >= WIN:
            return True
        else:
            return False

    def checkDiagonal(self, row, col):
        tile = self.board[row][col]
        nTiles = 1
        i = row - 1
        j = col + 1

        while i >= 0 and j < COLS:
            if self.board[i][j] == tile:
                nTiles += 1
                if nTiles == WIN:
                    return True
                i -= 1
                j += 1
            else:
                break

        i = row + 1
        j = col - 1

        while i < ROWS and j >= 0:
            if self.board[i][j] == tile:
                nTiles += 1
                if nTiles == WIN:
                    return True
                i += 1
                j -= 1
            else:
                break

        if nTiles >= WIN:
          return True
        
        nTiles = 1
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if self.board[i][j] == tile:
                nTiles += 1
                if nTiles == WIN:
                    return True
                i -= 1
                j -= 1
            else:
                break

        i = row + 1
        j = col + 1

        while i < ROWS and j < ROWS:
            if self.board[i][j] == tile:
                nTiles += 1
                if nTiles == WIN:
                    return True
                i += 1
                j += 1
            else:
                break

        if nTiles >= WIN:
            return True
        else:
            return False
      
    def printBoard(self):
        boardStr = ""

        for i in range(ROWS):
            lineStr = "\n| "
            for j in range(COLS):
                lineStr += self.board[i][j] + " | "
            boardStr = lineStr + boardStr

        boardStr = "| 0 | 1 | 2 | 3 | 4 | 5 | 6 |" + boardStr

        print(boardStr)
