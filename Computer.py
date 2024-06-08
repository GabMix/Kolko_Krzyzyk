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
    
