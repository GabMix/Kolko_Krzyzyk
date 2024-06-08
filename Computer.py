from random import randrange

from game import *

class Computer:
    def __init__(self, BoardSize, difficulty_lvl): # 0 - poczatkujacy, 1 - zaawansowany
        self.difficulty = difficulty_lvl
        self.game = Game(BoardSize)

    def easy_comp_move(self): #Ruch komputera w trybie początkującym
        #self.game.makeMove(randrange(self.game.boardSize), randrange(self.game.boardSize))
        if self.game.board[randrange(self.game.boardSize)][randrange(self.game.boardSize)] != 0:
            self.game.board[randrange(self.game.boardSize)][randrange(self.game.boardSize)] = self.game.activePlayer

        self.game.checkIfGameOver()
        if self.game.state == 0:
            self.game.switchPlayer()
        else:
            self.game.endGame()
    
    def minimax(self, depth, computer_turn : bool):
        self.game.checkIfGameOver()
        if self.game.state == -1:
            return 0
        elif self.game.state == 1:
            return 1
        elif self.game.state == 2:
            return -1

        if computer_turn == 1: #Sprawdzanie maksymalnego wyniku dla komputera
            best_score = -2
            for y in range(self.game.boardSize):
                for x in range(self.game.boardSize):
                    if self.game.board[y][x] == 0:
                        self.game.board[y][x] = self.game.activePlayer
                    score = self.minimax( depth + 1, False)
                    self.game.board[y][x] = 0
                    best_score = max(score, best_score)
            return best_score

        elif computer_turn == 1: #Sprawdzanie minimalneg wyniku dla gracza
            best_score = -2
            for y in range(self.game.boardSize):
                for x in range(self.game.boardSize):
                    if self.game.board[y][x] == 0:
                        self.game.switchPlayer()
                        self.game.board[y][x] = self.game.activePlayer
                        self.game.switchPlayer()
                    score = self.minimax( depth + 1, True)
                    self.game.board[y][x] = 0
                    best_score = min(score, best_score)
            return best_score

        self.game.checkIfGameOver()
        if self.game.state == 0:
            self.game.switchPlayer()
        else:
            self.game.endGame()
