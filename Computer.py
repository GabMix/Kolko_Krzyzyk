from random import randrange

from game import *

class Computer:
    def __init__(self, BoardSize, difficulty_lvl): # 0 - poczatkujacy, 1 - zaawansowany
        self.difficulty = difficulty_lvl
        self.game = Game(BoardSize)

    
