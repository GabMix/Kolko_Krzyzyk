from tkinter import messagebox
import tkinter as tk
from game import Game
from Computer import Computer

class GameBoard:
    def __init__(self, boardsize, ai_player): # 0 - easy, 1 - hard, 2 - no AI
        self.root = tk.Tk()
        self.root.geometry("1024x1024")
        self.root.title("Gra " + str(boardsize) + "x" + str(boardsize))
        self.game = Game(boardsize)
        self.ai_player = ai_player
        self.computer = None
        if ai_player != 2:
            self.computer = Computer(boardsize, self.game)

        for i in range(boardsize):
            self.root.rowconfigure(i, weight=1)
            self.root.columnconfigure(i, weight=1)

        self.btn = [[tk.Button(self.root, text='', font=('Arial', 24), command=lambda x1=x, y1=y: self.clickTile(x1, y1)) for x in range(boardsize)] for y in range(boardsize)]

        for x in range(boardsize):
            for y in range(boardsize):
                self.btn[y][x].grid(row=y, column=x, sticky="news")

        self.refresh()
        self.root.mainloop()

    def refresh(self):
        for x in range(self.game.boardSize):
            for y in range(self.game.boardSize):
                if self.game.board[y][x] == 1:
                    self.btn[y][x].config(text="X", state='disabled')
                elif self.game.board[y][x] == 2:
                    self.btn[y][x].config(text="O", state='disabled')
                else:
                    self.btn[y][x].config(text="", state='normal')

        print("Game board after refresh:")
        for row in self.game.board:
            print(row)

        if self.game.state != 0:
            self.endingAction()


    def clickTile(self, x, y):
        self.game.makeMove(x, y)
        self.refresh()
        if self.game.state == 0 and self.ai_player in (0, 1):
            if self.ai_player == 0:
                self.computer.easy_comp_move()
            elif self.ai_player == 1:
                self.computer.hard_comp_move()
            self.refresh()

    def endingAction(self):
        if self.game.state == 1:
            messagebox.showinfo("Game Over", "Winner is X!")
        elif self.game.state == 2:
            messagebox.showinfo("Game Over", "Winner is O!")
        else:
            messagebox.showinfo("Game Over", "Tie")
        self.root.destroy()

if __name__ == "__main__":
    GameBoard(3, 2)
