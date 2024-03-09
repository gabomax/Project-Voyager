import pygame
from properties import Properties

properties = Properties()

class Missions(pygame.sprite.Sprite) :
    
    def __init__(self, state, inventory, progress) :
        super().__init__()
        self.WIDTH, self.HEIGHT = properties.WIDTH // 8 * 2, properties.HEIGHT // 8 * 4
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.TURQUOISE)
        self.rect = self.image.get_rect()
        self.rect.center = (properties.WIDTH // 8 * 7, properties.HEIGHT // 8 * 6)
        
        self.state = state
        self.inventory = inventory
        self.progress = progress
        
        self.mission1 = False
        self.mission1_money = 100
        self.mission1_WIDTH, self.mission1_HEIGHT = properties.WIDTH // 8 * 7 - 100, properties.HEIGHT // 8 * 5 + 27
        
        self.mission2 = False
        self.mission2_fuel = 1000
        self.mission2_WIDTH, self.mission2_HEIGHT = properties.WIDTH // 8 * 7 - 100, properties.HEIGHT // 8 * 6 + 15
        
        self.mission3 = False
        self.mission3_mine = 50
        self.mission3_WIDTH, self.mission3_HEIGHT = properties.WIDTH // 8 * 7 - 100, properties.HEIGHT // 8 * 7 
            
    def show_missions(self) :
        properties.draw_text(f"Obtain {self.mission1_money} money", properties.BLACK, self.mission1_WIDTH, self.mission1_HEIGHT)
        properties.draw_text(f"Obtain {self.mission2_fuel} fuel", properties.BLACK, self.mission2_WIDTH, self.mission2_HEIGHT)
        properties.draw_text(f"Have {self.mission3_mine} mine", properties.BLACK, self.mission3_WIDTH, self.mission3_HEIGHT)
            
    def check_missions(self) :
        if self.state.state_n < 7 :
            if self.inventory.all_money >= self.mission1_money :
                self.mission1 = False
                self.mission1_money += 300 * ((self.progress.progress + 1) * 2)
                self.inventory.add_token()
                properties.draw_text(f"Obtain {self.mission1_money} money", properties.BLACK, self.mission1_WIDTH, self.mission1_HEIGHT)
            
            if self.inventory.all_fuel >= self.mission2_fuel :
                self.mission2 = False
                self.mission2_fuel += 1000 * ((self.progress.progress + 1) * 2)
                self.inventory.add_token()
                properties.draw_text(f"Obtain {self.mission2_fuel} fuel", properties.BLACK, self.mission2_WIDTH, self.mission2_HEIGHT)
            
            if self.inventory.mine >= self.mission3_mine :
                self.mission3 = False
                self.mission3_mine += 10 * ((self.progress.progress + 1) * 2)
                self.inventory.add_token()
                properties.draw_text(f"Have {self.mission3_mine} mine", properties.BLACK, self.mission3_WIDTH, self.mission3_HEIGHT)
        else :
            self.progress.add_progress()
            self.state.state_n = 1