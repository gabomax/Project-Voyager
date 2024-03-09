import pygame
import pygame_gui

pygame.init()

class Properties :
    
    def __init__(self) :
        self.WIDTH, self.HEIGHT = 1080, 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Project Voyager")
        self.font = pygame.font.Font(None, 36)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.PURPLE = (155, 0, 155)
        self.TURQUOISE = (0, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.PINK = (255, 0, 255)
        
        self.manager = pygame_gui.UIManager((self.WIDTH, self.HEIGHT))
        
        self.all_sprites = pygame.sprite.Group()
        self.item = pygame.sprite.Group()
        
    def draw_text(self, text, color, x, y) :
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, (x, y))
        
    def add_sprites(self, sprite) :
        self.all_sprites.add(sprite)
        
    def add_item(self, sprite) :
        self.item.add(sprite)
        
    def draw_sprites(self) :
        self.all_sprites.draw(self.screen)
        self.item.draw(self.screen)