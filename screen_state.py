import pygame
import pygame_gui
from properties import Properties

properties = Properties()

class ScreenState(pygame.sprite.Sprite) :
    
    def __init__(self, manager) :
        super().__init__()
        self.WIDTH, self.HEIGHT = properties.WIDTH // 8 * 4, properties.HEIGHT // 8 * 2
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (properties.WIDTH // 8 * 4, properties.HEIGHT // 8 * 7)
        
        self.state = 1
        
        self.abilities_button = pygame_gui.elements.UIButton(
                                             relative_rect=pygame.Rect((properties.WIDTH // 8 * 4, properties.HEIGHT // 8 * 7 - self.HEIGHT // 2), (self.WIDTH // 2, self.HEIGHT // 2)),
                                             text='hello',
                                             manager=manager)
        
        self.rocket_button = pygame_gui.elements.UIButton(
                                             relative_rect=pygame.Rect((properties.WIDTH // 8 * 4 - self.WIDTH // 2, properties.HEIGHT // 8 * 7 - self.HEIGHT // 2), (self.WIDTH // 2, self.HEIGHT // 2)),
                                             text='',
                                             manager=manager)
        
        self.rocket_button.image = pygame.image.load('assets/void.png')
        self.abilities_button.image = pygame.image.load('assets/void.png')
        
    def check_button(self, event) :
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.abilities_button :
                self.change_state(2)
            elif event.ui_element == self.rocket_button :
                self.change_state(1)
                
    def set_image(self) :
        self.rocket_button.image = pygame.image.load('assets/void.png')
        self.abilities_button.image = pygame.image.load('assets/void.png')
        
    def change_state(self, state) :
        self.state = state