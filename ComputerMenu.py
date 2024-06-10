import tkinter as tk
from Game_Board import GameBoard

class ComputerMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("Wybór trybu gry z komputerem")

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        #self.btn_easy = tk.Button(self.root, text="Tryb Latwy", command=self.easy_ai)
        #self.btn_hard = tk.Button(self.root, text="Tryb Zaawansowany", command=self.hard_ai)

        self.image_easy = tk.PhotoImage(file="IMG_20240609_021140.png")

        self.btn_easy = tk.Button(self.root, image=self.image_easy, borderwidth=0, command=lambda: self.easy_ai())
        self.btn_easy.place(x=100, y=50, width=300, height=200)

        self.image_hard = tk.PhotoImage(file="IMG_20240609_021210.png")

        self.btn_hard = tk.Button(self.root, image=self.image_hard, borderwidth=0, command=lambda: self.hard_ai())
        self.btn_hard.place(x=100, y=250, width=300, height=200)

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
