import tkinter as tk
from tkinter import messagebox
from game import *

class GameBoard:
    def __init__(self, boardsize, withTime=False):
        self.root = tk.Tk()
        # self.root.wm_attributes('-transparentcolor', self.root['bg'])
        self.root.geometry("768x768")
        self.root.title("Gra " + str(boardsize) + "x" + str(boardsize))
        self.root.resizable(False, False)
        self.game = Game(boardsize)

        self.timePerMove = 5
        self.timeX = self.timePerMove
        self.timeO = self.timePerMove

        # Tlo
        self.background_image = tk.PhotoImage(file="3x3-gotowe.png")
        self.background = tk.Label(self.root, image=self.background_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        self.withTime = withTime
        self.digitsImages = [tk.PhotoImage(file=str(i) + ".png") for i in range(0, 10)]

        self.digitHeight = 64
        self.digitWidth = 46
        span = 2

        self.timerXDigit1 = tk.Label(self.root, image=self.digitsImages[0], bg="black")
        self.timerXDigit1.place(x=315, y=35, width=self.digitWidth, height=self.digitHeight)
        self.timerXDigit0 = tk.Label(self.root, image=self.digitsImages[0], bg="black")
        self.timerXDigit0.place(x=315 + self.digitWidth + span, y=35, width=self.digitWidth, height=self.digitHeight)

        self.timerODigit1 = tk.Label(self.root, image=self.digitsImages[0], bg="black")
        self.timerODigit1.place(x=325 + 2 * (self.digitWidth + span), y=35, width=self.digitWidth,
                                height=self.digitHeight)
        self.timerODigit0 = tk.Label(self.root, image=self.digitsImages[0], bg="black")
        self.timerODigit0.place(x=325 + 3 * (self.digitWidth + span), y=35, width=self.digitWidth,
                                height=self.digitHeight)

        # Tworzenie przyciskow
        self.off_image = tk.PhotoImage(file="Empty_temp.png")
        self.btn = [[tk.Button(self.root, image=self.off_image, borderwidth=0, activebackground='black')
                     for i in range(boardsize)] for j in range(boardsize)]
        # Przypisywanie przyciskow do siatki
        for x in range(boardsize):
            for y in range(boardsize):
                self.btn[x][y].place(x=223 + (330 / boardsize) * x, y=300 + (330 / boardsize) * y,
                                     width=300 / boardsize, height=300 / boardsize)
                self.btn[y][x].config(command=lambda x1=x, y1=y: self.clickTile(x1, y1))

        # Odpowiedni rozmiar znaków
        self.X_image = tk.PhotoImage(file="X_" + str(boardsize) + ".png")
        self.O_image = tk.PhotoImage(file="O_" + str(boardsize) + ".png")

        if self.withTime:
            self.timerHandler = self.root.after(1000, lambda: self.clock())

        self.refresh()
        self.root.mainloop()

    def clock(self):
        self.countDown()
        if self.timeX < 0 or self.timeO < 0:
            self.game.switchPlayer()
            self.resetTime()

        self.refresh()
        self.timerHandler = self.root.after(1000, lambda: self.clock())

    def resetTime(self):
        self.timeX = self.timePerMove
        self.timeO = self.timePerMove

    def countDown(self):
        if self.game.activePlayer == 1:
            self.timeX -= 1
        elif self.game.activePlayer == 2:
            self.timeO -= 1

    def refresh(self):
        for x in range(self.game.boardSize):
            for y in range(self.game.boardSize):
                if self.game.board[y][x] == 1:
                    self.btn[y][x].config(image=self.X_image)
                elif self.game.board[y][x] == 2:
                    self.btn[y][x].config(image=self.O_image)
                else:
                    self.btn[y][x].config(image=self.off_image)
        self.refreshTimer()
        if self.game.state != 0:
            self.endingAction()

    def clickTile(self, x, y):
        before = self.game.board[y][x]
        self.game.makeMove(x, y)
        after = self.game.board[y][x]

        if before != after and self.withTime:
            self.resetTime()
            self.root.after_cancel(self.timerHandler)
            self.timerHandler = self.root.after(1000, lambda: self.clock())

        self.refresh()

    def endingAction(self):
        if self.withTime:
            self.root.after_cancel(self.timerHandler)
        if self.game.state == 1:
            messagebox.showinfo("Game Over", "Winner is X!")
        elif self.game.state == 2:
            messagebox.showinfo("Game Over", "Winner is O!")
        else:
            messagebox.showinfo("Game Over", "Tie")
        self.root.destroy()
        from Main_Menu import MainMenu
        MainMenu()

    def refreshTimer(self):
        if self.withTime == False:
            return

        self.timerXDigit0.config(image=self.digitsImages[self.timeX % 10])
        self.timerXDigit1.config(image=self.digitsImages[int(self.timeX / 10)])
        self.timerODigit0.config(image=self.digitsImages[self.timeO % 10])
        self.timerODigit1.config(image=self.digitsImages[int(self.timeO / 10)])
