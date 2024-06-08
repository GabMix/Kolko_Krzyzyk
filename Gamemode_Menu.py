from Game_Board import *

class Choose:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("768x768")
        self.root.title("Wybór trybu gry")
        self.root.resizable(False, False)

        # Tło
        self.background_image = tk.PhotoImage(file="Gamemode_Background.png")
        self.background = tk.Label(self.root, image=self.background_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        # Wybór rozmiaru
        self.image_3x3 = tk.PhotoImage(file="3x3_btn.png")
        self.btn_3x3 = tk.Button(self.root, image=self.image_3x3 , borderwidth=0, command=self.run_3x3)
        self.btn_3x3.place(x=350, y=300, width=100, height=100)

        self.image_4x4 = tk.PhotoImage(file="4x4_btn.png")
        self.btn_4x4 = tk.Button(self.root, image=self.image_4x4, borderwidth=0, command=self.run_4x4)
        self.btn_4x4.place(x=450, y=300, width=100, height=100)

        self.image_5x5 = tk.PhotoImage(file="5x5_btn.png")
        self.btn_5x5 = tk.Button(self.root, image=self.image_5x5, borderwidth=0, command=self.run_5x5)
        self.btn_5x5.place(x=550, y=300, width=100, height=100)

        # Wybór gry na czas
        self.btn_time_3x3 = tk.Button(self.root, image=self.image_3x3, borderwidth=0, command=lambda: self.run_time_game(3))
        self.btn_time_3x3.place(x=350, y=400, width=100, height=100)

        self.btn_time_4x4= tk.Button(self.root, image=self.image_4x4, borderwidth=0, command=lambda: self.run_time_game(4))
        self.btn_time_4x4.place(x=450, y=400, width=100, height=100)

        self.btn_time_5x5 = tk.Button(self.root, image=self.image_5x5, borderwidth=0, command=lambda: self.run_time_game(5))
        self.btn_time_5x5.place(x=550, y=400, width=100, height=100)

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

    def run_time_game(self, board_size):
        print("time game", board_size)