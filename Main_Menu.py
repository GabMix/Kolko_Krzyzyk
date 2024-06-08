from Gamemode_Menu import *

class MainMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1024x1024")
        self.root.title("Kółko i Krzyżyk")
        self.root.resizable(False, False)
        # Tlo + Ramka
        self.background_image = tk.PhotoImage(file="mainmenu.png")
        self.background = tk.Label(self.root, image=self.background_image)
        self.background.place(x=0, y=0, relwidth=1, relheight=1)

        # Start
        self.btn_start_image = tk.PhotoImage(file="start_btn.png")
        self.btn_start = tk.Button(self.root, image=self.btn_start_image, borderwidth=0, activebackground='black', command=self.run_choose_game)
        self.btn_start.place(x=512-199, y=330, width=398, height=115)

        # Statystyki
        self.btn_statystyki_image = tk.PhotoImage(file="statystyki_btn.png")
        self.btn_statystyki = tk.Button(self.root, image=self.btn_statystyki_image, borderwidth=0, activebackground='black', command=self.run_statystyki)
        self.btn_statystyki.place(x=512-199, y=330+150, width=398, height=115)

        # Twórcy
        self.btn_tworcy_image = tk.PhotoImage(file="tworcy_btn.png")
        self.btn_tworcy = tk.Button(self.root, image=self.btn_tworcy_image, borderwidth=0, activebackground='black', command=self.run_tworcy)
        self.btn_tworcy.place(x=512-199, y=330+300, width=398, height=115)


        self.root.mainloop()
        self.root.quit()

    def run_choose_game(self):
        self.root.destroy()
        Choose()

    def run_statystyki(self):
        print("ERROR: Statystyki nie gotowe")

    def run_tworcy(self):
        print("ERROR: Twórcy nie gotowe")
