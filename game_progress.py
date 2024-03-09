import pygame
from properties import Properties

properties = Properties()

class GameProgress(pygame.sprite.Sprite) :
    
    def __init__(self) :
        super().__init__()
        self.WIDTH, self.HEIGHT = properties.WIDTH, properties.HEIGHT // 8
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (properties.WIDTH // 8 * 4, properties.HEIGHT // 16)
        
        self.progress = 0
        
    def add_progress(self) :
        self.progress += 1
        
    def draw_progress(self) :
        properties.draw_text(f"Progress {self.progress}%", properties.BLACK, properties.WIDTH // 8 * 4, properties.HEIGHT // 16)