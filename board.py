import pygame
from colours import Colours

class Board:
    def __init__(self, rows, cols, num_colours):
        self.num_rows = rows
        self.num_cols = cols
        self.current_row = 0
        self.current_col = 0
        self.cell_size = 50
        self.board = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colours = Colours.get_cell_colours()[0:num_colours]
        self.key_pegs = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.kp_colours = Colours.get_keypeg_colours()
        self.count = 0
        self.guessed = False
        self.game_over = False

    #Debugging
    def print_board(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.board[row][column], end='')
            print()


    def update_board(self, colour, code):
        self.board[self.current_row][self.current_col] = self.colours.index(colour)
        if self.current_col < (self.num_cols - 1):
            self.current_col += 1
        
    def draw(self, screen):
        for row in range(self.num_rows):
            kp_cell_rect = pygame.Rect(((self.num_cols)*self.cell_size) + 26, row*self.cell_size, 
                                       self.cell_size, self.cell_size - 2)
            pygame.draw.rect(screen, Colours.darkGrey, kp_cell_rect)
            for column in range(self.num_cols):
                if column % 2 == 0:
                    kp_x_multiplier = 0.25
                else:
                    kp_x_multiplier = 0.75
                if column > 1:
                    kp_y_multiplier = 0.75
                else:
                    kp_y_multiplier = 0.25

                cell_value = self.board[row][column]
                kp_cell_value = self.key_pegs[row][column]
                cell_rect = pygame.Rect((column*self.cell_size) + 25, row*self.cell_size, 
                                        self.cell_size, self.cell_size - 2) 
                pygame.draw.rect(screen, Colours.darkGrey, cell_rect)
                pygame.draw.circle(screen, self.colours[cell_value], ((column*self.cell_size) + (0.5*self.cell_size) + 25, 
                                                                   (row*self.cell_size) + (0.5*self.cell_size)), 15)
                pygame.draw.circle(screen, self.kp_colours[kp_cell_value],(((self.num_cols)*self.cell_size) + (kp_x_multiplier*self.cell_size) + 26,
                                   (row*self.cell_size) + (kp_y_multiplier*self.cell_size)), 7.5)

