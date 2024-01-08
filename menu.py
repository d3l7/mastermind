import pygame, sys, time
from colours import Colours
from buttons import MenuButton
from guess import Guess

class Menu:
    def __init__(self, font, game):
        self.buttons = []
        self.text = font.render('Mastermind', True, Colours.white)
        self.textRect = self.text.get_rect()
        self.game = game
        self.played = False

        self.textRect.center = (150, 40)
        
    def change_flag(self):
        self.game.running = True
        time.sleep(0.1)

        if not self.played:
            self.game.board.create_board(self.game.guesses, 4, self.game.num_colours + 1)
            self.game.guess = Guess(self.game.board, self.game.code)
        else:
            self.game.reset()

        self.game.board.colours = Colours.get_cell_colours()[0:self.game.num_colours + 1]
        self.game.create_buttons(self.game.board.colours)
        if self.game.code == []:
            self.game.create_code()

    def create_buttons(self):
        startGame = MenuButton(75, 150, 160, 50, pygame.font.Font(None, 20) , Colours.darkGrey, 'Start game', self.change_flag)
        blankButton = MenuButton(75, 225, 160, 50, pygame.font.Font(None, 20) , Colours.darkGrey, 'Blanks: ', self.game.change_blanks)
        dupesButton = MenuButton(75, 300, 160, 50, pygame.font.Font(None, 20) , Colours.darkGrey, 'Duplicates: ', self.game.change_duplicates)
        guessesButton = MenuButton(75, 375, 160, 50, pygame.font.Font(None, 20) , Colours.darkGrey, 'Number of guesses: ', self.game.change_guesses)
        coloursButton = MenuButton(75, 450, 160, 50, pygame.font.Font(None, 20) , Colours.darkGrey, 'Number of colours: ', self.game.change_num_colours)
        quitGame = MenuButton(75, 525, 160, 50, pygame.font.Font(None, 20) , Colours.darkGrey, 'Quit game', self.quit_game)
        
        self.buttons = [startGame, blankButton, dupesButton, quitGame, guessesButton, coloursButton]

    def run(self, screen):
        screen.fill(Colours.darkBlue)
        screen.blit(self.text, self.textRect)

        for button in self.buttons:
            button.process(screen)

        if self.game.blanks:
            self.blanks = pygame.font.Font(None, 20).render('On', True, Colours.white)
        else:
            self.blanks = pygame.font.Font(None, 20).render('Off', True, Colours.white)
        if self.game.duplicates:
            self.dupes = pygame.font.Font(None, 20).render('On', True, Colours.white)
        else:
            self.dupes = pygame.font.Font(None, 20).render('Off', True, Colours.white)

        self.guesses = pygame.font.Font(None, 20).render(f'{self.game.guesses}', True, Colours.white)
        self.colours = pygame.font.Font(None, 20).render(f'{self.game.num_colours}', True, Colours.white)

        self.blanksRect = self.blanks.get_rect()
        self.dupesRect = self.dupes.get_rect()
        self.guessesRect = self.guesses.get_rect()
        self.coloursRect = self.colours.get_rect()

        self.textRect.center = (150, 40)
        self.blanksRect.center = (190, 249)
        self.dupesRect.center = (200, 324)
        self.guessesRect.center = (220, 399)
        self.coloursRect.center = (220, 474)

        screen.blit(self.blanks, self.blanksRect)
        screen.blit(self.dupes, self.dupesRect)
        screen.blit(self.guesses, self.guessesRect)
        screen.blit(self.colours, self. coloursRect)


    def quit_game(self):
        pygame.quit()
        sys.exit()

        

        


