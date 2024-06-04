from Game_Board import *

class Choose:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("768x768")
        self.root.title("Wybór trybu gry")

        # Tymczasowy design ------------------------------------
        boardsize = 3
        # Tworzenie siatki
        for i in range(boardsize):
            self.root.rowconfigure(i, weight=1)
            self.root.columnconfigure(i, weight=1)

        # Tworzenie przyciskow
        self.btn = [[tk.Button(self.root, text="Tymczasowy design") for i in range(boardsize)] for j in range(boardsize)]
        # Przypisywanie przyciskow do siatki
        for x in range(boardsize):
            for y in range(boardsize):
                self.btn[x][y].grid(row=y, column=x, sticky="news")  # news = north east west south
        self.btn[0][0].configure(text="3x3", command=self.run_3x3)
        self.btn[1][0].configure(text="4x4", command=self.run_4x4)
        self.btn[2][0].configure(text="5x5", command=self.run_5x5)

        # koniec tymczasowego designu ------------------------------

        self.root.mainloop()

    def run_3x3(self):
        self.root.destroy()
        GameBoard(3)

    def run_4x4(self):
        self.root.destroy()
        GameBoard(4)

    def run_5x5(self):
        self.root.destroy()
        GameBoard(5)