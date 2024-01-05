import pygame, sys
from colours import Colours
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

game.create_buttons()
menu.create_buttons()

#Game loop
while True:
    #Allows the user to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            sys.exit()

    screen.fill(Colours.darkBlue)

    #Drawing
    if menu.running == True:
        menu.run(screen)
    else:
        screen.fill(Colours.darkBlue)
        game.run(screen)
    
    """game.draw(screen)
    if not (game.board.guessed or game.board.game_over):
        for button in game.buttons:
            button.process(screen, game.code)"""

    pygame.display.flip()

    #Set frame-rate to 60fps
    clock.tick(60)

