import tkinter as tk
from tkinter import messagebox
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
                self.btn[y][x].grid(row=y, column=x, sticky="news") # news = north east west south
                self.btn[y][x].config(command=lambda x1=x,y1=y: self.clickTile(x1, y1))

        self.refresh()
        self.root.mainloop()

    def refresh(self):
        for x in range(self.game.boardSize):
            for y in range(self.game.boardSize):
                if self.game.board[y][x] == 1:
                    self.btn[y][x].config(text="X")
                elif self.game.board[y][x] == 2:
                    self.btn[y][x].config(text="O")
                else:
                    self.btn[y][x].config(text="")

        if self.game.state != 0:
            self.endingAction()

    def clickTile(self, x, y):
        self.game.makeMove(x, y)
        self.refresh()

    def endingAction(self):
        if self.game.state == 1:
            messagebox.showinfo("Game Over", "Winner is X!")
        elif self.game.state == 2:
            messagebox.showinfo("Game Over", "Winner is O!")
        else:
            messagebox.showinfo("Game Over", "Tie")
        self.root.destroy()