import pygame
from properties import Properties

properties = Properties()

class MainScreen(pygame.sprite.Sprite) :
    
    def __init__(self, state) :
        super().__init__()
        
        self.state = state
        
        self.WIDTH, self.HEIGHT = properties.WIDTH // 8 * 4, properties.HEIGHT // 8 * 5
        self.image = self.state.state
        self.rect = self.image.get_rect()
        self.rect.center = (properties.WIDTH // 8 * 4, properties.HEIGHT // 8 * 2.5 + (properties.HEIGHT //8))
    
class State() :

    def __init__(self) :

        self.st1 = pygame.image.load('assets/state 1.png')
        self.st2 = pygame.image.load('assets/state 2.png')
        self.st3 = pygame.image.load('assets/state 3.png')
        self.st4 = pygame.image.load('assets/state 4.png')
        self.st5 = pygame.image.load('assets/state 5.png')
        self.st6 = pygame.image.load('assets/state 6.png')
        self.st7 = pygame.image.load('assets/state 7.png')

        self.state_n = 1
        self.state = self.st1

    def reset(self) :
        self.state = self.st1
        self.state_n = 1

    def change_state(self) :
        self.state_n += 1

        if self.state_n == 1 :
            self.state = self.st1
        elif self.state_n == 2 :
            self.state = self.st2
        elif self.state_n == 3 :
            self.state = self.st3
        elif self.state_n == 4 :
            self.state = self.st4
        elif self.state_n == 5 :
            self.state = self.st5
        elif self.state_n == 6 :
            self.state = self.st6
        elif self.state_n == 7 :
            self.state = self.st7

    def getState(self) :
        return self.state