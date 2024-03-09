import pygame
from properties import Properties

properties = Properties()

class ScreenState(pygame.sprite.Sprite) :
    
    def __init__(self) :
        super().__init__()
        self.WIDTH, self.HEIGHT = properties.WIDTH // 8 * 4, properties.HEIGHT // 8 * 2
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (properties.WIDTH // 8 * 4, properties.HEIGHT // 8 * 7)
        