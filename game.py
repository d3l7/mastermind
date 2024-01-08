import pygame, random, time
from board import Board
from buttons import *
from guess import Guess
from colours import Colours


class Game:
    def __init__(self):
        self.num_colours = 6
        self.guesses = 8
        self.blanks = False
        self.duplicates = False
        self.running = False
        self.board = Board()
        self.code = []
        self.buttons = []
        self.colours = Colours.get_cell_colours()[1:self.num_colours]


        self.board.create_board(self.guesses, 4, self.num_colours)
        self.guess = Guess(self.board, self.code)

    def run(self, screen):
        screen.fill(Colours.darkBlue)
        self.board.draw(screen)

        if self.code == []:
            self.create_code()

        if not (self.board.guessed or self.board.game_over):
            for button in self.buttons:
                 button.process(screen, self.code)
        elif self.board.guessed:
            text = pygame.font.Font(None, 50).render('You win!', True, Colours.white)
            textRect = text.get_rect()
            textRect.center = (150, 625)
            
            screen.blit(text, textRect)

            MenuButton(25, 650, 100, 30, pygame.font.Font(None, 20), self.board.colours[0], 
                                        'Play again', self.reset).process(screen)
            MenuButton(175, 650, 100, 30, pygame.font.Font(None, 20), self.board.colours[0], 
                                        'Return to menu', self.change_flag).process(screen)
        elif self.board.game_over:
            text = pygame.font.Font(None, 50).render('Game over', True, Colours.white)
            textRect = text.get_rect()
            textRect.center = (150, 625)
            
            screen.blit(text, textRect)

            MenuButton(25, 650, 100, 20, pygame.font.Font(None, 20), self.board.colours[0], 
                                        'Play again', self.reset).process(screen)
            MenuButton(175, 650, 100, 20, pygame.font.Font(None, 20), self.board.colours[0], 
                                        'Return to menu', self.change_flag).process(screen)

    def create_buttons(self, colours):
        offsetx = 25
        offsety = 625

        for i in range(1, self.num_colours + 1):
            self.buttons.append(ColourButton(offsetx, offsety, 25, 25, pygame.font.Font(None, 40), colours[i], 
                                             '', self.board.update_board ))
            offsetx += 25

        self.buttons.append(Button(25, 660, 100, 30, pygame.font.Font(None, 20), colours[0], 
                                        'Submit guess', self.guess.award_key_pegs))
        self.buttons.append(Button(175, 660, 100, 30, pygame.font.Font(None, 20), colours[0], 
                                        'Undo', self.board.undo))
        
    def reset(self):
        self.board.reset(self.guesses)
        self.guess = Guess(self.board, self.code)
        self.code = []
        time.sleep(0.1)
    
    def change_flag(self):
        self.running = False
        time.sleep(0.1)

    def change_blanks(self):
        if self.blanks:
            self.blanks = False
        else:
            self.blanks = True
        time.sleep(0.1)

    def change_duplicates(self):
        if self.duplicates:
            self.duplicates = False
        else:
            self.duplicates = True
        time.sleep(0.1)
    
    def change_guesses(self):
        if self.guesses == 12:
            self.guesses = 6
        else: 
            self.guesses += 1
        time.sleep(0.1)
        
    def change_num_colours(self):
        if self.num_colours > 9:
            self.num_colours -= 6
        else:
            self.num_colours += 1
        time.sleep(0.1)


    def create_code(self):
        numbers = []
        if self.blanks:
            for i in range(0, self.num_colours):
                numbers.append(i)
        else:
            for i in range(1, self.num_colours + 1):
                numbers.append(i)
        for i in range(4):
            rand_int = random.choice(numbers)
            self.code.append(rand_int)
            if not self.duplicates:
                del numbers[numbers.index(rand_int)]




            



