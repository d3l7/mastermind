import pygame, sys
from colours import Colours
from buttons import MenuButton
from game import Game
from menu import Menu

#Initialise pygame
pygame.init()

title_font = pygame.font.Font(None, 40)

#Display screen and window title
screen = pygame.display.set_mode((300, 700))
pygame.display.set_caption('Mastermind')

clock = pygame.time.Clock()

game = Game()
menu = Menu(title_font, game)

#Create buttons outside of game loop so that we aren't creating 60 buttons a second.
menu.create_buttons()
#Game loop
while True:
    #Allows the user to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            menu.quit_game()

    #Run the menu or game
    if not game.running:
        screen.fill(Colours.darkBlue)
        menu.run(screen)
    else:
        screen.fill(Colours.darkBlue)    #Since the menu is always the first thing displayed on the screen, we need to clear the screen via refilling again
        if not menu.played:
            menu.played = True   
        game.run(screen)
    
    pygame.display.flip()

    #Set frame-rate to 60fps
    clock.tick(60)

