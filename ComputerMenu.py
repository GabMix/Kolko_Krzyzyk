import tkinter as tk
from Game_Board import GameBoard
from Computer import Computer

class ComputerMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Wybór trybu gry z komputerem")
        self.ai_player = None

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        self.btn_easy = tk.Button(self.root, text="Tryb Latwy", command=self.easy_ai)
        self.btn_hard = tk.Button(self.root, text="Tryb Zaawansowany", command=self.hard_ai)

        self.btn_easy.grid(row=0, sticky="news")
        self.btn_hard.grid(row=1, sticky="news")

        self.root.mainloop()

    def easy_ai(self):
        self.root.destroy()
        #self.ai_player = Computer(3, 0)  # Store AI instance
        GameBoard(3, 0)

    def hard_ai(self):
        self.root.destroy()
        #self.ai_player = Computer(3, 1)  # Store AI instance
        GameBoard(3, 1)

if __name__ == "__main__":
    ComputerMenu()
