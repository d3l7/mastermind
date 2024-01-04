import pygame, sys
from colours import Colours
from game import Game

#Initialise pygame
pygame.init()

title_font = pygame.font.Font(None, 40)

#Display screen and window title
screen = pygame.display.set_mode((300, 700))
pygame.display.set_caption('Mastermind')

clock = pygame.time.Clock()

game = Game()
game.create_buttons()
game.create_code()
game.board.print_board()

print(game.code)
#Game loop
while True:
    #Allows the user to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            sys.exit()


    #Drawing
    screen.fill(Colours.darkBlue)

    game.draw(screen)
    if game.board.guessed == False:
        for button in game.buttons:
            button.process(screen, game.code)
    
    pygame.display.flip()

    #Set frame-rate to 60fps
    clock.tick(60)

