class Game:
    def __init__(self, boardSize):
        self.board = []
        self.boardSize = boardSize

        for i in range(boardSize):
            self.board.append([])
            for j in range(boardSize):
                self.board[i].append(0)