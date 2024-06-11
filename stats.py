import tkinter as tk
import json
import os
    # def run_statystyki(self):
    #     self.show_stats()
class Stats:
    def load_stats(self):
        if os.path.exists("stats.json"):
            with open("stats.json", "r") as file:
                return json.load(file)
        return {"Wins": {"Player 1": 0, "Player 2": 0}, "Losses": {"Player 1": 0, "Player 2": 0}, "Draws": 0}
    
    def save_stats(self, stats):
        with open("stats.json", "w") as file:
            json.dump(stats, file)
    
    def show_stats(self):
        stats = self.load_stats()
        stats_window = tk.Toplevel(self.root)
        stats_window.geometry("400x300")
        stats_window.title("Statystyki")
    
        wins_label = tk.Label(stats_window,
                                text=f"Wygrane:\nPlayer 1: {stats['Wins']['Player 1']}\nPlayer 2: {stats['Wins']['Player 2']}")
        wins_label.pack()
    
        losses_label = tk.Label(stats_window,
                                text=f"Przegrane:\nPlayer 1: {stats['Losses']['Player 1']}\nPlayer 2: {stats['Losses']['Player 2']}")
        losses_label.pack()
    
        draws_label = tk.Label(stats_window, text=f"Remisy: {stats['Draws']}")
        draws_label.pack()
    
        back_button = tk.Button(stats_window, text="Powrót do menu", command=self.back_to_main_menu)
        back_button.pack()
    
    def update_stats(self, result):
        stats = self.load_stats()
        if result == -1:
            stats["Draws"] += 1
        else:
            winner = "Player 1" if result == 1 else "Player 2"
            loser = "Player 2" if result == 1 else "Player 1"
            stats["Wins"][winner] += 1
            stats["Losses"][loser] += 1
        self.save_stats(stats)
    
    def back_to_main_menu(self):
        self.root.destroy()
        self.__init__()
    
    # if __name__ == "__main__":
    #     main_menu = MainMenu()



