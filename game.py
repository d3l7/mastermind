import pygame, random, time
from board import Board
from buttons import *
from guess import Guess
from colours import Colours


class Game:
    def __init__(self):
        self.num_colours = 10
        self.board = Board(12, 4, self.num_colours + 1) 
        self.guess = Guess(self.board)
        self.code = []
        self.buttons = []

    def run(self, screen):
        screen.fill(Colours.darkBlue)
        self.board.draw(screen)
        if self.code == []:
            self.create_code()

        if not (self.board.guessed or self.board.game_over):
            for button in self.buttons:
                 button.process(screen, self.code)


        
    def create_buttons(self):
        offsetx = 25
        offsety = 625

        for i in range(1, self.num_colours + 1):
            self.buttons.append(ColourButton(offsetx, offsety, 25, 25, pygame.font.Font(None, 40), self.board.colours[i], 
                                             '', self.board.update_board ))
            offsetx += 25

        self.buttons.append(Button(25, 650, 100, 50, pygame.font.Font(None, 20), self.board.colours[0], 
                                        'Submit guess', self.guess.award_key_pegs))
        self.buttons.append(Button(125, 650, 100, 50, pygame.font.Font(None, 20), self.board.colours[0], 
                                        'Undo', self.board.undo))

    def create_code(self):
        for i in range(4):
            self.code.append(random.randint(1, self.num_colours))



            



