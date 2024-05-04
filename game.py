class Game:
    def __init__(self, boardSize):
        self.board = []
        self.boardSize = boardSize
        self.activePlayer = 1
        self.state = 0  # 0 - in progress; 1 - X won, 2 - Y won, -1 - tie

        for i in range(boardSize):
            self.board.append([])
            for j in range(boardSize):
                self.board[i].append(0)

    def makeMove(self, x, y):
        if x >= self.boardSize or y >= self.boardSize:
            return
        
        if self.board[x][y] != 0:
            return

        if self.state != 0:
            return

        self.board[x][y] = self.activePlayer

        self.checkIfGameOver()
        #TODO: zmienić gracza

    #TODO: sprawidzić czy jest remis, opowiednio zmienić stan gry (self.state), należy sprawdzić kolumny, wiersze i proste, uwzględnić rozmiary planszy
    #TODO: sprawdzić czy któryś gracz wygrał, zmienić stan gry
    def checkIfGameOver(self):
        print("")

