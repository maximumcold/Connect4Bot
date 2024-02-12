import Player
import pygame
import Board

#* PascalCase for classes
class HumanPlayer:
    
    def __init__(self, color, cell_size):
        self.color = color
        self.cell_size = cell_size
    
    
    def get_move(self, board, screen):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, _ = pygame.mouse.get_pos()
                        row = mouse_x // self.cell_size
                        running = False
                        return row
            screen.fill('white')
            board.draw_board(screen, self.cell_size)
            pygame.display.flip()
    