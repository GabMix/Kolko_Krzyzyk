import tkinter as tk
from tkinter import messagebox
from game import *

class GameBoard:
    def __init__(self, boardsize):
        self.root = tk.Tk()
        self.root.geometry("768x768")
        self.root.title( "Gra " + str(boardsize) + "x" + str(boardsize) )
        self.root.resizable(False, False)
        self.game = Game(boardsize)

        # Tlo
        self.background_image = tk.PhotoImage(file="3x3-gotowe.png")
        self.background = tk.Label(self.root, image=self.background_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        # Tworzenie przyciskow
        self.off_image = tk.PhotoImage(file="Empty_temp.png")
        self.btn = [[tk.Button(self.root, image=self.off_image, borderwidth=0, activebackground='black')
                     for i in range(boardsize)] for j in range(boardsize)]
        # Przypisywanie przyciskow do siatki
        for x in range(boardsize):
            for y in range(boardsize):
                self.btn[x][y].place(x=223 + (330/boardsize)*x, y=300 + (330/boardsize)*y, width=300/boardsize, height=300/boardsize)
                self.btn[y][x].config(command=lambda x1=x,y1=y: self.clickTile(x1, y1))

        # Odpowiedni rozmiar znaków
        self.X_image = tk.PhotoImage(file="X_"+str(boardsize)+".png")
        self.O_image = tk.PhotoImage(file="O_"+str(boardsize)+".png")

        self.refresh()
        self.root.mainloop()

    def refresh(self):
        for x in range(self.game.boardSize):
            for y in range(self.game.boardSize):
                if self.game.board[y][x] == 1:
                    self.btn[y][x].config(image=self.X_image)
                elif self.game.board[y][x] == 2:
                    self.btn[y][x].config(image=self.O_image)
                else:
                    self.btn[y][x].config(image=self.off_image)

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
