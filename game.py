import pygame, random
from board import Board
from buttons import *
from guess import Guess


class Game:
    def __init__(self):
        self.num_colours = 6
        self.board = Board(12, 4, self.num_colours + 1) 
        self.guess = Guess(self.board)
        self.code = []
        self.buttons = []

    def draw(self, screen):
        self.board.draw(screen)
        

    def create_buttons(self):
        offsetx = 25
        offsety = 625

        for i in range(1, self.num_colours + 1):
            self.buttons.append(ColourButton(offsetx, offsety, 25, 25, pygame.font.Font(None, 40), self.board.colours[i], '', self.board.update_board ))
            offsetx += 25

        self.buttons.append(GuessButton(25, 650, 100, 50, pygame.font.Font(None, 20), self.board.colours[0], 'Submit guess', self.guess.award_key_pegs))

    def create_code(self):
        for i in range(4):
            self.code.append(random.randint(1, self.num_colours))



            



