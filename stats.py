import json
import os
import tkinter as tk


class Stats:
    def __init__(self, root):
        self.root = root

    def load_stats(self):
        if os.path.exists("stats.json"):
            with open("stats.json", "r") as file:
                return json.load(file)
        return {"Wins": {"Gracz 1": 0, "Gracz 2": 0}, "Losses": {"Gracz 1": 0, "Gracz 2": 0}, "Draws": 0}

    def save_stats(self, stats):
        with open("stats.json", "w") as file:
            json.dump(stats, file)

    def show_stats(self):
        stats = self.load_stats()
        stats_window = tk.Toplevel(self.root)
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
