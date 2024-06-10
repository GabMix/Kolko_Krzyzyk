from random import randrange
from game import Game
from copy import deepcopy

class Computer:
    def __init__(self, BoardSize, gameObj: Game): # 0 - easy, 1 - hard
        self.game = gameObj

    def easy_comp_move(self):
        while True:
            x, y = randrange(self.game.boardSize), randrange(self.game.boardSize)
            if self.game.board[y][x] == 0:
                self.game.board[y][x] = 2 #self.game.activePlayer
                break
        self.game.checkIfGameOver()
        if self.game.state == 0:
            self.game.switchPlayer()
        else:
            self.game.endGame()


    def minimax(self, depth, is_maximizing, board):
        original_state = self.game.state
        #self.game.checkIfGameOver()
        if self.game.state == 1:
            self.game.state = original_state
            return -1
        elif self.game.state == 2:
            self.game.state = original_state
            return 1
        elif self.game.state == -1:
            self.game.state = original_state
            return 0


        if is_maximizing:
            best_score = -100
            new_board = deepcopy(board)  # Deep copy the board
            for y in range(2):
                for x in range(2):
                    if board[y][x] == 0:
                    #    self.game.board[y][x] = 2
                    #    score = self.minimax(depth + 1, False)
                    #    self.game.board[y][x] = 0
                        new_board[y][x] = 2  # Place move on copy
                        score = self.minimax(depth + 1, False, new_board)
                        new_board[y][x] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 100
            new_board = deepcopy(board)  # Deep copy the board
            for y in range(2):
                for x in range(2):
                    if board[y][x] == 0:
                        #self.game.board[y][x] = 1
                        #score = self.minimax(depth + 1, True)
                        #self.game.board[y][x] = 0
                        new_board[y][x] = 1  # Place move on copy
                        score = self.minimax(depth + 1, True, new_board)
                        new_board[y][x] = 0
                        best_score = min(score, best_score)
            return best_score

    def hard_comp_move(self):
        print("Hard AI making a move...")
        best_score = -100
        best_move = None
        for y in range(self.game.boardSize):
            for x in range(self.game.boardSize):
                if self.game.board[y][x] == 0:
                    self.game.board[y][x] = 2 #self.game.activePlayer
                    score = self.minimax(0, False, self.game.board)
                    self.game.board[y][x] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)
        if best_move:
            self.game.makeMove(best_move[0], best_move[1])
            print(f"Hard AI chose position: {best_move}")
        self.game.checkIfGameOver()
        #if self.game.state == 0:
        #    self.game.switchPlayer()
        #else:
        #    self.game.endGame()
