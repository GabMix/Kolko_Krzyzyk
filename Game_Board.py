import tkinter as tk
from tkinter import messagebox
from game import *
from Computer import Computer
from stats import Stats

class GameBoard:
    def __init__(self, boardsize, ai_player, withTime=False): # 0 -Łatwy, 1- Trydny, 2- Brak
        self.root = tk.Tk()
        #self.stats = Stats(self.root)
        # self.root.wm_attributes('-transparentcolor', self.root['bg'])
        self.root.geometry("768x768")
        self.root.title("Gra " + str(boardsize) + "x" + str(boardsize))
        self.root.resizable(False, False)
        self.game = Game(boardsize)

        self.ai_player = ai_player
        self.computer = None
        if ai_player != 2:
            self.computer = Computer(boardsize, self.game)

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
        elif self.ai_player == 2:
            self.last_move = (-1, -1)
            self.reset_status = 0
            self.btn_reset = tk.Button(self.root, text='reset', borderwidth=0, command=self.resetMove)
            self.btn_reset.place(x=650, y=400, width=80, height=80)

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
        self.refresh()
        if self.game.state == 0 and self.ai_player in (0, 1):
            if self.ai_player == 0:
                self.computer.easy_comp_move()
            elif self.ai_player == 1:
                self.computer.hard_comp_move()
            self.refresh()
        after = self.game.board[y][x]

        if self.withTime==False and self.ai_player==2:
            self.last_move = (x, y)
            self.reset_status = 0
            self.btn_reset.config(text='reset')

        if before != after and self.withTime:
            self.resetTime()
            self.root.after_cancel(self.timerHandler)
            self.timerHandler = self.root.after(1000, lambda: self.clock())

        self.refresh()

    def endingAction(self):
        if self.withTime:
            self.root.after_cancel(self.timerHandler)
        #self.stats.update_stats(self.game.state)
        if self.game.state == 1:
            messagebox.showinfo("Game Over", "Winner is X!")
        elif self.game.state == 2:
            messagebox.showinfo("Game Over", "Winner is O!")
        else:
            messagebox.showinfo("Game Over", "Tie")
        stats = Stats(self.root)
        stats.update_stats(self.game.state)

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

    def resetMove(self):
        if self.last_move != (-1, -1) and self.reset_status == 0:
            self.game.board[self.last_move[1]][self.last_move[0]] = 0
            self.btn[self.last_move[1]][self.last_move[0]].config(image=self.off_image)
            self.game.switchPlayer()
            self.btn_reset.config(text='X')
            self.reset_status = 1
