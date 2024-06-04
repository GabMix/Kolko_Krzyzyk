import tkinter as tk
from game import *

class GameBoard:
    def __init__(self, boardsize):
        self.root = tk.Tk()
        self.root.geometry("1024x1024")
        self.root.title( "Gra " + str(boardsize) + "x" + str(boardsize) )
        self.game = Game(boardsize)

        # Tworzenie siatki
        for i in range(boardsize):
            self.root.rowconfigure(i, weight=1)
            self.root.columnconfigure(i, weight=1)

        # Tworzenie przyciskow
        self.btn = [[tk.Button(self.root, text=str(i)+str(j)) for i in range(boardsize)] for j in range(boardsize)]
        # Przypisywanie przyciskow do siatki
        for x in range(boardsize):
            for y in range(boardsize):
                self.btn[x][y].grid(row=y, column=x, sticky="news") # news = north east west south
                self.btn[x][y].config(command=lambda x1=x,y1=y: self.clickTile(x1, y1))

        self.refresh()
        self.root.mainloop()

    def refresh(self):
        for x in range(self.game.boardSize):
            for y in range(self.game.boardSize):
                if self.game.board[x][y] == 1:
                    self.btn[x][y].config(text="X")
                elif self.game.board[x][y] == 2:
                    self.btn[x][y].config(text="O")
                else:
                    self.btn[x][y].config(text="")

    def clickTile(self, x, y):
        self.game.makeMove(x, y)
        self.refresh()