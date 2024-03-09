import pygame
from properties import Properties

properties = Properties()

class Inventory(pygame.sprite.Sprite) :
    
    def __init__(self, state) :
        super().__init__()
        self.WIDTH, self.HEIGHT = properties.WIDTH // 8 * 2, properties.HEIGHT // 8 * 3
        self.image = pygame.Surface([self.WIDTH, self.HEIGHT])
        self.image.fill(properties.PURPLE)
        self.rect = self.image.get_rect()
        self.rect.center = (properties.WIDTH // 8 * 7, properties.HEIGHT // 8 * 2.5)
        
        self.state = state
        
        self.money = 0
        self.all_money = 0
        self.money_WIDTH, self.money_HEIGHT = properties.WIDTH // 8 * 7 - 40, properties.HEIGHT // 16 * 2
        
        self.fuel = 0
        self.all_fuel = 0
        self.fuel_price = 10
        self.fuel_WIDTH, self.fuel_HEIGHT = properties.WIDTH // 8 * 7 - 40, properties.HEIGHT // 8 * 2.5
        
        self.mine = 1
        self.mine_fuel_price = 300
        self.mine_money_price = 20
        self.mine_WIDTH, self.mine_HEIGHT = properties.WIDTH // 8 * 7 - 40, properties.HEIGHT // 8 * 3
        
        self.pieces = 0
        self.pieces_WIDTH, self.pieces_HEIGHT = properties.WIDTH // 8 * 7 - 40, properties.HEIGHT // 8 * 3.5
        
    def add_fuel(self, amount) :
        if self.money >= self.fuel_price :
            self.fuel += amount
            self.all_fuel += amount
            self.remove_money(self.fuel_price)
            self.change_fuel_price()
            
    def remove_fuel(self, amount) :
        self.fuel -= amount
        
    def change_fuel_price(self) :
        self.fuel_price += 1
            
    def add_mine(self) :
        if self.money >= self.mine_money_price and self.fuel >= self.mine_fuel_price :
            self.mine += 1
            self.remove_money(self.mine_money_price)
            self.remove_fuel(self.mine_fuel_price)
            self.change_mine_price()
            
    def change_mine_price(self) :
        self.mine_fuel_price += 1
        self.mine_money_price += 1
        
    def add_money(self, amount) :
        self.money += amount
        self.all_money += amount
        
    def remove_money(self, amount) :
        self.money -= amount
        
    def add_piece(self) :
        if self.state.state_n < 7 :
            self.pieces += 1
            self.state.change_state()
        
    def draw_inventory(self) :
        properties.draw_text(f"money : {self.money}", properties.BLACK, self.money_WIDTH, self.money_HEIGHT)
        properties.draw_text(f"fuel : {self.fuel}", properties.BLACK, self.fuel_WIDTH, self.fuel_HEIGHT)
        properties.draw_text(f"mine : {self.mine}", properties.BLACK, self.mine_WIDTH, self.mine_HEIGHT)
        properties.draw_text(f"pièces : {self.pieces}, {self.state.state_n}", properties.BLACK, self.pieces_WIDTH, self.pieces_HEIGHT)
