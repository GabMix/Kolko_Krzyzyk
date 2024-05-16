from Game_Board import *

class main_menu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1024x1024")
        self.root.title("Kółko i Krzyżyk")
        self.root.resizable(False, False)
        self.background_image = tk.PhotoImage(file = "mainmenu.png")
        self.background = tk.Label(self.root, image=self.background_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        # Start
        self.btn_start_image = tk.PhotoImage(file = "start_btn_temp.png")
        self.btn_start = tk.Button(self.root, image=self.btn_start_image, command=self.run_3x3)
        self.btn_start.place(x=340, y=340, width=400, height=120)

        # Opcje
        self.btn_opcje_image = tk.PhotoImage(file="start_btn_temp.png")
        self.btn_opcje = tk.Button(self.root, image=self.btn_opcje_image, command=self.run_4x4)
        self.btn_opcje.place(x=340, y=485, width=400, height=120)

        # Twórcy
        self.btn_tworcy_image = tk.PhotoImage(file="start_btn_temp.png")
        self.btn_tworcy = tk.Button(self.root, image=self.btn_tworcy_image, command=self.run_5x5)
        self.btn_tworcy.place(x=340, y=625, width=400, height=120)


        self.root.mainloop()

    def run_3x3(self):
        Game(3)

    def run_4x4(self):
        Game(4)

    def run_5x5(self):
        Game(5)


def main():

    main_menu()

    return 0

main()