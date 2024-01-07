import pygame
from button import Button

class ColourButton(Button):
    def __init__(self, x, y, width, height, font, colour, buttonText='', onclickFunction = None, onePress = False):
        super().__init__(x, y, width, height, font, colour, buttonText, onclickFunction, onePress)

    def process(self, screen, code):
        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColours['normal'])

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColours['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColours['pressed'])
                if self.onePress:
                    self.onclickFunction(self.colour)
                
                elif not self.alreadyPressed:
                    self.onclickFunction(self.colour)
                    self.alreadyPressed = True
                
            else:
                self.alreadyPressed = False
                
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2, 
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
                                                  ])
        
        screen.blit(self.buttonSurface, self.buttonRect)

class MenuButton(Button):
    def __init__(self, x, y, width, height, font, colour, buttonText='', onclickFunction = None, onePress = False):
        super().__init__(x, y, width, height, font, colour, buttonText, onclickFunction, onePress)
    
    def process(self, screen):
        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColours['normal'])

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColours['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColours['pressed'])
                if self.onePress:
                    self.onclickFunction()
                
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
                
            else:
                self.alreadyPressed = False
                
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2, 
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
                                                  ])
        
        screen.blit(self.buttonSurface, self.buttonRect)