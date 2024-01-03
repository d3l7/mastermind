import pygame
from colours import Colours

class Button:
    def __init__(self, x, y, width, height, font, colour, buttonText='', onclickFunction = None, onePress = False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.colour = colour

        self.fillColours = {'normal': self.colour,
                            'hover' : self.colour,
                             'pressed': self.colour}
        
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

    def process(self, screen, code):
        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColours['normal'])

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColours['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColours['pressed'])
                if self.onePress:
                    self.onclickFunction(self.colour, code)
                
                elif not self.alreadyPressed:
                    self.onclickFunction(self.colour, code)
                    self.alreadyPressed = True
                
            else:
                self.alreadyPressed = False
                
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2, 
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
                                                  ])
        
        screen.blit(self.buttonSurface, self.buttonRect)
