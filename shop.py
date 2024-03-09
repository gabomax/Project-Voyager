import pygame
import pygame_gui
from properties import Properties

properties = Properties()

class Shop(pygame.sprite.Sprite) :
    
    def __init__(self, manager) :
        super().__init__()
        self.WIDTH, self.HEIGHT = properties.WIDTH // 8 * 2, properties.HEIGHT // 8 * 3
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (properties.WIDTH // 8, properties.HEIGHT // 8 * 2.5)
        
        self.fuel_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((properties.WIDTH // 16 - self.WIDTH // 6 // 2, properties.HEIGHT // 16 * 3 - self.HEIGHT // 6 // 2), (self.WIDTH // 6, self.HEIGHT // 6)),
                                             text='Fuel',
                                             manager=manager)
        
        self.mine_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((properties.WIDTH // 16 * 2 - self.WIDTH // 6 // 2, properties.HEIGHT // 16 * 3 - self.HEIGHT // 6 // 2), (self.WIDTH // 6, self.HEIGHT // 6)),
                                             text='Mine',
                                             manager=manager)
        
        self.fuel = Item((properties.WIDTH // 16, properties.HEIGHT // 16 * 3), self.WIDTH // 6, self.HEIGHT // 6)
        self.mine = Item((properties.WIDTH // 16 * 2, properties.HEIGHT // 16 * 3), self.WIDTH // 6, self.HEIGHT // 6)
                
    def buy(self, inventory, event) :
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.fuel_button :
                inventory.add_fuel(100)
            if event.ui_element == self.mine_button :
                inventory.add_mine()
        elif event.type == pygame.MOUSEBUTTONDOWN :
                inventory.add_money(1)


class Item(pygame.sprite.Sprite) :
    
    def __init__(self, initial_position, width, height) :
        super().__init__()
        self.WIDTH, self.HEIGHT = width, height
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = initial_position