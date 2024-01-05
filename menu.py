import pygame
from colours import Colours
from buttons import MenuButton

class Menu:
    def __init__(self, font, game):
        self.buttons = []
        self.running = True
        self.text = font.render('Mastermind', True, Colours.white)
        self.textRect = self.text.get_rect()
        self.game = game

        self.textRect.center = (150, 40)

    def change_flag(self):
        self.running = False

    def create_buttons(self):
        self.buttons = [MenuButton(75, 200, 150, 50, pygame.font.Font(None, 20) , Colours.darkGrey, 'Start game', self.change_flag)]

    def run(self, screen):
        screen.blit(self.text, self.textRect)

        for button in self.buttons:
            button.process(screen)

        


