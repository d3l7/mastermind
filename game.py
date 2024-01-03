import pygame, random
from board import Board
from button import Button


class Game:
    def __init__(self):
        self.num_colours = 6
        self.board = Board(12, 4, self.num_colours) 
        self.code = []
        self.buttons = []

    def draw(self, screen):
        self.board.draw(screen)

    def create_buttons(self):
        offsetx = 25
        offsety = 650

        for i in range(1, self.num_colours + 1):
            self.buttons.append(Button(offsetx, offsety, 25, 25, pygame.Font(None, 40), self.board.colours[i], '', self.board.update_board ))
            offsetx += 25

    def create_code(self):
        for i in range(4):
            self.code.append(random.randint(1, self.num_colours+1))



            



