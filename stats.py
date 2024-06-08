import json
import os


#updatujemy stats wygranych remisow i przegranych
def update_stats(self, result):
    stats = self.load_stats()
    if result =="Draw":  #moge zmienic na polskie (?) 
        stats["Draws"] = stats.get("Draws", 0)+1
    else:
        stats["Wins"][self.players[result]] = stats["Wins"].get(self.players[result], 0) +1
        loser ="Player 2" if self.players[result] == "Player 1" else "Player 1"
        stats["Losses"][loser] =stats["Losses"].get(loser, 0)+1
    self.save_stats(stats)


#zapisywanie statystyk
def load_stats(self):
    if os.path.exists("stats.json"):
        with open("stats.json", "r") as file:
            return json.load(file)
    return {"Wins": {}, "Losses": {}, "Draws": 0}


def save_stats(self, stats):
    with open("stats.json", "w") as file:
        json.dump(stats, file)



