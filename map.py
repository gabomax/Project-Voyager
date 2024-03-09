import pygame
from properties import Properties

properties = Properties()

class Map(pygame.sprite.Sprite) :
    
    def __init__(self) :
        super().__init__()
        self.WIDTH, self.HEIGHT = properties.WIDTH // 8 * 2, properties.HEIGHT // 8 * 4
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (properties.WIDTH // 8, properties.HEIGHT // 8 * 6)