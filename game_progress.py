import pygame
from properties import Properties

properties = Properties()

class GameProgress(pygame.sprite.Sprite) :
    
    def __init__(self) :
        super().__init__()
                
        self.progress = 0
        
        self.WIDTH, self.HEIGHT = properties.WIDTH / 100, properties.HEIGHT // 8 // 3 + 2
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, properties.HEIGHT // 8 // 3)
            
    def set_width(self) :
        self.WIDTH = ((properties.WIDTH / 100) * self.progress )
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.GREEN)
        
    def add_progress(self) :
        self.progress += 1
        
    def draw_progress(self) :
        properties.draw_text(f"Progress {self.progress}%", properties.BLACK, properties.WIDTH // 8 * 4 - 70, properties.HEIGHT // 16)