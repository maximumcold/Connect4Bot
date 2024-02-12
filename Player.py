from abc import ABC
import random

BLACK = -1
RED = 1

class Player(ABC):
    
    def __init__(self, player_color):
        self.color = player_color
    
    def get_move(self, board, screen):
        return random.randint(0, 7)

    