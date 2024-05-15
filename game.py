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

        if self.board[y][x] != 0:
            return

        if self.state != 0:
            return

        self.board[y][x] = self.activePlayer

        self.checkIfGameOver()
        if self.state == 0:
            self.switchPlayer()
        else:
            self.endGame()
        #TODO: zmienić gracza

    #TODO: sprawidzić czy jest remis, opowiednio zmienić stan gry (self.state), należy sprawdzić kolumny, wiersze i przekątne, uwzględnić rozmiary planszy
    #TODO: sprawdzić czy któryś gracz wygrał, zmienić stan gry
    def checkWin(self):
        #rzędy,
        global i
        for y in range(self.boardSize):
            for i in range(self.boardSize):
                if self.board[i][y] != self.activePlayer:
                    break
                elif i == (self.boardSize - 1):
                    self.state = self.activePlayer
        #kolumny
        for x in range(self.boardSize):
            for i in range(self.boardSize):
                if self.board[x][i] != self.activePlayer:
                    break
                elif i == (self.boardSize - 1):
                    self.state = self.activePlayer
        #przekatne_1
        for i in range(self.boardSize):
            if self.board[i][i] != self.activePlayer:
                break
            elif i == (self.boardSize - 1):
                self.state = self.activePlayer
        #przekatne_2
        for i in range(self.boardSize):
            if self.board[i][(self.boardSize - 1) - i] != self.activePlayer:
                break
            elif i == (self.boardSize - 1):
                self.state = self.activePlayer

    def checkTie(self):
        if 0 not in self.board:
            self.state = -1
    def checkIfGameOver(self):
        self.checkTie()
        self.checkWin()
        if self.state != 0:
            print("Gra zakonczona")
    def switchPlayer(self):
        if self.activePlayer == 1:
            self.activePlayer = 2
        else:
            self.activePlayer = 1
    def endGame(self):
        if self.state == -1:
            print("Gra konczy sie remisem, pocwicz :)")
        elif self.state == 1:
            print("Gra konczy sie wygrana X, gratulacje!")
        elif self.state == 2:
            print("Gra konczy sie wygrana O, gratulacje!")

