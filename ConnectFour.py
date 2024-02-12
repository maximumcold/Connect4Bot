import pygame
import sys
from Board import Board 
from Player import Player
from HumanPlayer import HumanPlayer
from AIPlayer import AIPlayer
import timeit
import time
import random

BLACK = -1
RED = 1

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Connect 4!")
running = True
turn = 1
has_played = False

# Get that board boi
board = Board()
grid_rows = 6
grid_cols = 7
cell_size = min(screen_width // grid_cols, screen_height // grid_rows)  

# Adds players to the game
# Passes in cell_size for ease of access
player_red = AIPlayer(cell_size, RED)
player_black = AIPlayer(cell_size, BLACK)

# Makes a current player so that the game has to check whose turn it is
current_player = player_red


# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        # Checks if the player being passed in is an AI or a human player
        vaild_moves = board.find_all_valid_moves()
        
        
        moves = [0,0,0,0,0,0,0]
        start = timeit.timeit()
        
        for i in range(len(vaild_moves)):
            moves[i] = current_player.get_move(board, screen)
            if moves[i] > 0:
                break
        
        
        y = max(moves)
        print(moves)
        if y == 0:
            index_y = random.randrange(0,6)
        else:
            index_y = moves.index(y)
        #print(moves)
        #time.sleep(1)
        # Checks if the selected column is valid and can be played on
        if board.is_valid_move(index_y):  
            
            # Plays move
            start = timeit.timeit()
            board.play_move(index_y, current_player.player_int)
            end = timeit.timeit()
            #print(end - start)
            # Checks the board to see if there is a win
            check_board = board.check_win(board.board_state())
            if check_board == 0:
                print("Draw")
                
            if check_board == 1:
                print("RED wins")
            if check_board == -1:
                print("BLACK wins")
            
            # Sets the turn for player 2
            current_player = player_black if current_player is player_red else player_red
            
            #* TEMP: prints out a list of all the possible valid moves
            #print(board.find_all_valid_moves())
        
    screen.fill('white')
    board.draw_board(screen, cell_size)
    pygame.display.flip()
    