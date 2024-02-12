import math
import pygame
import random
from Board import Board
import time
class AIPlayer:
    def __init__(self, cell_size, player_int):
        self.cell_size = cell_size
        self.player_int = player_int
    
    def get_move(self, board: Board, screen):
        board_copy = board.make_copy()
        best_move = self.minimax(board_copy, 5, self.player_int) # player num either -1 or 1
        return best_move
    
    def minimax(self, board_copy: Board, depth, player_int):
        
        valid_locations = board_copy.find_all_valid_moves()
        
        # Check to see if there is a win
        if depth == 0 or board_copy.isterminal():
            
            if board_copy.check_win(board_copy.board_state) is not None and board_copy.check_win(board_copy.board_state()) != 0:
                return board_copy.check_win(board_copy.board_state)
                
            elif board_copy.check_win(board_copy.board_state) is None:
                return 0
            else:
                return 0
                
        value = -math.inf
        i = 0
        
        for i in range(len(valid_locations)):
            if valid_locations[i] != 0:
                if board_copy.is_valid_move(i):
                    board_copy.play_move(i, player_int)
                    new_score = self.minimax(board_copy, depth - 1, -player_int) 
            
                if new_score * self.player_int >= value:
                        value = new_score
        #print(value)
        return value
        
        
        
        
        
        
        
        
        
        
        
        
        
        # else:
        #     value = math.inf
        #     best_move = None
            
        #     for column in valid_locations:
        #         board_copy = board.make_copy()
        #         if board_copy.is_valid_move(column):
        #             board_copy.play_move(column, self.color)
        #             new_score = self.minimax(board_copy, depth - 1, True)
        #         if new_score < value:
        #             value = new_score
                    
        #     return value


 # if depth == 0 or board.isterminal():
        #     if board.check_win(board.board_state()) == 1 and minimax_player:
        #         return None, 100000000000
        #     # Handle if the next move the other player can play is a win
        #     elif board.check_win(board.board_state()) == -1 and not minimax_player:
        #         return None, -100000000000
        #     else:
        #         return None, 0
                    
# if depth == 0 or board.isterminal():
#             print("In loop")
#         # Check to see if there is a win
#             if minimax_player:
#                     if board.check_win(board.board_state() == -1):
#                         return None, -1000000000
#                     elif board.check_win(board.board_state() == 1):
#                         return None, 1000000000
                
#                 # Handle if the next move the other player can play is a win
#             elif not minimax_player:
#                 if board.check_win(board.board_state() == 1):
#                     return None, 1000000000
#                 elif board.check_win(board.board_state() == -1):
#                     return None, -1000000000
#             else:
#                 return None, 0