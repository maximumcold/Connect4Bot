import pygame
from scipy.signal import convolve2d
import numpy as np
import copy

class Board:
    #* is this right
    BOARD_HEIGHT = 6
    BOARD_WIDTH = 7
    def __init__(self, board= None):
        if board is None:
            self.game_board = [[0 for _ in range(7)] for _ in range(6)]
        else:
            self.game_board = board
    # Return the current state of the board
    def board_state(self):
        game_board_state = self.game_board
        return game_board_state
    
    def make_copy(self):
        board_copy = Board(copy.deepcopy(self.game_board))
        return board_copy
    
    # Checks for a win condition
    def check_win(self, current_board_state):
        # Check rows
        current_board_state = self.board_state()
        valid_moves  = self.find_all_valid_moves()
        
        tiles_red = 0
        tiles_black = 0
        # Check for win rows
        for x in range(len(self.game_board)):
            for y in range(len(self.game_board[0])):
                if tiles_red == 4:
                    return 1
                if tiles_black == 4:
                    return -1
                if current_board_state[x][y] == 1:
                    tiles_red += 1
                else:
                    tiles_red = 0
                if current_board_state[x][y] == -1:
                    tiles_black += 1
                else:
                    tiles_black = 0
        
                    
        # Check Columns for win
        for y in range(len(self.game_board[0])):
            for x in range(len(self.game_board)):
                if tiles_red == 4:
                    return 1
                if tiles_black == 4:
                    return -1
                if current_board_state[x][y] == 1:
                    tiles_red += 1
                else:
                    tiles_red = 0
                if current_board_state[x][y] == -1:
                    tiles_black += 1
                else:
                    tiles_black = 0
                    
        # Check Diagonal for red (player 1) diagonal
        for x in range(len(self.game_board) - 3):
            for y in range(len(self.game_board[0]) - 3):
                if (self.game_board[x][y] == 1 and
                    self.game_board[x+1][y+1] == 1 and
                    self.game_board[x+2][y+2] == 1 and
                    self.game_board[x+3][y+3] == 1):
                    return 1
        for x in range(len(self.game_board)):
            for y in range(len(self.game_board[0]) - 3):
                if (self.game_board[x][y] == 1 and
                    self.game_board[x-1][y+1] == 1 and
                    self.game_board[x-2][y+2] == 1 and
                    self.game_board[x-3][y+3] == 1):
                    return 1
        
        # Check if black (playe 2) win diagonal
        for x in range(len(self.game_board) - 3):
            for y in range(len(self.game_board[0]) - 3):
                if (self.game_board[x][y] == -1 and
                    self.game_board[x+1][y+1] == -1 and
                    self.game_board[x+2][y+2] == -1 and
                    self.game_board[x+3][y+3] == -1):
                    return -1
        for x in range(len(self.game_board)):
            for y in range(len(self.game_board[0]) - 3):
                if (self.game_board[x][y] == -1 and
                    self.game_board[x-1][y+1] == -1 and
                    self.game_board[x-2][y+2] == -1 and
                    self.game_board[x-3][y+3] == -1):
                    return -1
                
        if len(valid_moves) == 0:
            return 0
              
        return None
    
    def isterminal(self):
        if len(self.find_all_valid_moves()) == 0:
            return True
        return False
    
    # Checks if the passed in y is a valid move (the column isn't full)
    def is_valid_move(self, y):
        return self.gets_bottom(y) is not None
            
    # Plays the move (if valid)
    def play_move(self, y, color):
        if self.is_valid_move(y):
            bottom = self.gets_bottom(y)
            self.game_board[bottom][y] = color
            
        else:
            print("invalid move at {}".format(y))
            # raise ValueError("Invalid Move")

    # Finds the bottom of the passed in column, returns None otherwise
    def gets_bottom(self, y):
        # Starting from the bottom of the colmun, iterates up until it find an open space
        for i in range(self.BOARD_HEIGHT - 1, -1, -1):
            if self.game_board[i][y] == 0:
                return i
        return None
    
    # Switches the gravity so that blocks fall to a different side (not complete)
    def switch_gravity(self):
        pass
    
    # Draws the game board
    def draw_board(self, screen, cell_size):  
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[0])):
                pygame.draw.line(screen, 'black', (0, i * cell_size), (700, i * cell_size))
                pygame.draw.line(screen, 'black', (j * cell_size, 0,), (j * cell_size, 600))
    
        for row in range(len(self.game_board)):
            for col in range(len(self.game_board[0])):
                if self.game_board[row][col] == 1:
                    rect_x = col * cell_size
                    rect_y = row * cell_size
                    pygame.draw.rect(screen, 'red', (rect_x, rect_y, cell_size, cell_size))
                
                if self.game_board[row][col] == -1:
                    rect_x = col * cell_size
                    rect_y = row * cell_size
                    pygame.draw.rect(screen, 'black', (rect_x, rect_y, cell_size, cell_size))

    # Returns a list of all possible moves (the y values)
    def find_all_valid_moves(self):
        moves = [0] * 7
        for y in range(7):
            if self.is_valid_move(y):
                moves[y] = -1
        return moves