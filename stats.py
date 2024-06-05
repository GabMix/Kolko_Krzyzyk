import json
import os

# #sprawdza czy gracz wygral
# def check_if_winner(self):
#     #rzedy
#     for row in range(self.boardsize):
#         if all(self.board[row][col]== self.player for col in range(self.boardsize)):
#             return True
#     #kolumny
#     for col in range(self.boardsize):
#         if all(self.board[row][col]==self.player for row in range(self.boardsize)):
#             return True
#     #przekatna1 lg do pd
#     if all(self.board[i][i] ==self.player for i in range(self.boardsize)):
#         return True
#     #przekątna2 pg ld
#     if all(self.board[i][self.boardsize- 1-i] == self.player for i in range(self.boardsize)):
#         return True
#     return False


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




