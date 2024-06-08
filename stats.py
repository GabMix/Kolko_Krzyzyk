import json
import os


#updatujemy stats wygranych remisow i przegranych
def update_stats(self, result):
    stats = self.load_stats()
    if result ==-1:  
        stats["Draws"]+=1
    else:
        stats["Wins"][self.players[result]] = stats["Wins"].get(self.players[result], 0) + 1
        loser = 2 if result == 1 else 1
        stats["Losses"][self.players[loser]] =stats["Losses"].get(self.players[loser],0)+1
    self.save_stats(stats)


#zapisywanie statystyk
def load_stats(self):
    if os.path.exists("stats.json"):
        with open("stats.json", "r") as file:
            return json.load(file)
    return {"Wins": {"Player 1": 0, "Player 2": 0}, "Losses": {"Player 1": 0, "Player 2": 0}, "Draws": 0}


def save_stats(self, stats):
    with open("stats.json", "w") as file:
        json.dump(stats, file)



