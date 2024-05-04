class Game:
    def __init__(self, boardSize):
        self.board = []
        self.boardSize = boardSize
        self.activePlayer = 1
        self.isFinished = False

        for i in range(boardSize):
            self.board.append([])
            for j in range(boardSize):
                self.board[i].append(0)

    def makeMove(self, x, y):
        if x >= self.boardSize or y >= self.boardSize:
            return

        self.board[x][y] = self.activePlayer