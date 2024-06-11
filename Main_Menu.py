from Gamemode_Menu import *
import tkinter as tk
import json
import os

class Stats:
    def load_stats(self):
        if os.path.exists("stats.json"):
            with open("stats.json", "r") as file:
                return json.load(file)
        return {"Wins": {"Gracz 1": 0, "Gracz 2": 0}, "Losses": {"Gracz 1": 0, "Gracz 2": 0}, "Draws": 0}

    def save_stats(self, stats):
        with open("stats.json", "w") as file:
            json.dump(stats, file)

    def show_stats(self, root):
        stats = self.load_stats()
        stats_window = tk.Toplevel(root)
        stats_window.geometry("400x300")
        stats_window.title("Statystyki")

        wins_label = tk.Label(stats_window,
                              text=f"Wygrane:\nGracz 1: {stats['Wins']['Gracz 1']}\nGracz 2: {stats['Wins']['Gracz 2']}")
        wins_label.pack()

        losses_label = tk.Label(stats_window,
                                text=f"Przegrane:\nGracz 1: {stats['Losses']['Gracz 1']}\nGracz 2: {stats['Losses']['Gracz 2']}")
        losses_label.pack()

        draws_label = tk.Label(stats_window, text=f"Remisy: {stats['Draws']}")
        draws_label.pack()

        back_button = tk.Button(stats_window, text="Powrót do menu", command=stats_window.destroy)
        back_button.pack()

    def update_stats(self, result):
        stats = self.load_stats()
        if result == -1:
            stats["Draws"] += 1
        else:
            winner = "Gracz 1" if result == 1 else "Gracz 2"
            loser = "Gracz 2" if result == 1 else "Gracz 1"
            stats["Wins"][winner] += 1
            stats["Losses"][loser] += 1
        self.save_stats(stats)


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
        #print("ERROR: Statystyki nie gotowe")
        stats = Stats()
        stats.show_stats(self.root)

    def run_tworcy(self):
       # print("ERROR: Twórcy nie gotowe")
        creators_window = tk.Toplevel(self.root)
        creators_window.title("Twórcy")
        creators_window.geometry("400x300")
        creators_window.configure(relief="flat")

        bigger_font = ("Helvetica", 12)

        creators_label = tk.Label(creators_window,
                                  text="Gaba Mikstein\nSebastian Mleko\nKrzysztof Mazurkiewicz\nPiotr Mlak\nDagmara Krenich",
                                  bg="white", font=bigger_font)
        creators_label.pack(fill="both", expand=True)
