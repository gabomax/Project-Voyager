import pygame
import pickle
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
        self.money_WIDTH, self.money_HEIGHT = properties.WIDTH // 8 * 7 - 128, properties.HEIGHT // 16 * 2 + 576
        
        self.token = 0
        self.token_WIDTH, self.token_HEIGHT = properties.WIDTH // 8 * 7 - 128, properties.HEIGHT // 16 * 2 + 599
        
        self.fuel = 0
        self.all_fuel = 0
        self.fuel_price = 10
        self.fuel_WIDTH, self.fuel_HEIGHT = properties.WIDTH // 8 * 7 - 70, properties.HEIGHT // 8 * 2.5 - 30
        
        self.mine = 1
        self.mine_fuel_price = 300
        self.mine_money_price = 20
        self.mine_WIDTH, self.mine_HEIGHT = properties.WIDTH // 8 * 7 - 70, properties.HEIGHT // 8 * 3 - 20
        
        self.pieces = 0
        self.pieces_price = 10
        self.pieces_WIDTH, self.pieces_HEIGHT = properties.WIDTH // 8 * 7 - 70, properties.HEIGHT // 8 * 3.5 - 10
        
    def save_money(self) :
        with open('money.pickle', 'wb') as f:
            pickle.dump(self.money, f)
        
    def load_money(self):
        try:
            with open('money.pickle', 'rb') as f:
                self.money = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.money = 0
            
    def save_all_money(self) :
        with open('max_money.pickle', 'wb') as f:
            pickle.dump(self.all_money, f)
        
    def load_all_money(self):
        try:
            with open('max_money.pickle', 'rb') as f:
                self.all_money = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.all_money = 0
            
    def save_fuel(self) :
        with open('fuel.pickle', 'wb') as f:
            pickle.dump(self.fuel, f)
        
    def load_fuel(self):
        try:
            with open('fuel.pickle', 'rb') as f:
                self.fuel = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.fuel = 0
            
    def save_all_fuel(self) :
        with open('all_fuel.pickle', 'wb') as f:
            pickle.dump(self.all_fuel, f)
        
    def load_all_fuel(self):
        try:
            with open('all_fuel.pickle', 'rb') as f:
                self.all_fuel = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.all_fuel = 0
            
    def save_mine(self) :
        with open('mine.pickle', 'wb') as f:
            pickle.dump(self.mine, f)
        
    def load_mine(self):
        try:
            with open('mine.pickle', 'rb') as f:
                self.mine = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mine = 0
            
    def save_token(self) :
        with open('token.pickle', 'wb') as f:
            pickle.dump(self.token, f)
        
    def load_token(self):
        try:
            with open('token.pickle', 'rb') as f:
                self.token = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.token = 0
            
    def save_pieces(self) :
        with open('pieces.pickle', 'wb') as f:
            pickle.dump(self.pieces, f)
        
    def load_pieces(self):
        try:
            with open('pieces.pickle', 'rb') as f:
                self.pieces = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.pieces = 0
            
    def save_fuel_price(self) :
        with open('fuel_price.pickle', 'wb') as f:
            pickle.dump(self.fuel_price, f)
        
    def load_fuel_price(self):
        try:
            with open('fuel_price.pickle', 'rb') as f:
                self.fuel_price = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.fuel_price = 0
            
    def save_mine_fuel_price(self) :
        with open('mine_fuel_price.pickle', 'wb') as f:
            pickle.dump(self.mine_fuel_price, f)
        
    def load_mine_fuel_price(self):
        try:
            with open('mine_fuel_price.pickle', 'rb') as f:
                self.mine_fuel_price = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mine_fuel_price = 0
            
    def save_mine_money_price(self) :
        with open('mine_money_price.pickle', 'wb') as f:
            pickle.dump(self.mine_money_price, f)
        
    def load_mine_money_price(self):
        try:
            with open('mine_money_price.pickle', 'rb') as f:
                self.mine_money_price = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mine_money_price = 0
            
    def save_state(self) :
        with open('state.pickle', 'wb') as f:
            pickle.dump(self.state.state_n, f)
            
    def load_state(self):
        try:
            with open('state.pickle', 'rb') as f:
                self.state.state_n = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.state.state_n = 0
            
    def save(self) :
        self.save_money()
        self.save_all_money()
        
        self.save_fuel()
        self.save_all_fuel()
        
        self.save_mine()
        self.save_mine_fuel_price()
        self.save_mine_money_price()
        
        self.save_pieces()
        
        self.save_token()
        
        self.save_state()
        
    def load(self) :
        self.load_money()
        self.load_all_money()
        
        self.load_fuel()
        self.load_all_fuel()
        
        self.load_mine()
        self.load_mine_fuel_price()
        self.load_mine_money_price()
        
        self.load_pieces()
        
        self.load_token()
        
        self.load_state()
        
        
    def add_fuel(self, amount) :
        if self.money >= self.fuel_price :
            self.fuel += amount
            self.all_fuel += amount
            self.remove_money(self.fuel_price)
            self.change_fuel_price()
            
    def remove_fuel(self, amount) :
        self.fuel -= amount
        
    def change_fuel_price(self) :
        self.fuel_price += 5
            
    def add_mine(self) :
        if self.money >= self.mine_money_price and self.fuel >= self.mine_fuel_price :
            self.mine += 1
            self.remove_money(self.mine_money_price)
            self.remove_fuel(self.mine_fuel_price)
            self.change_mine_price()
            
    def change_mine_price(self) :
        self.mine_fuel_price += 100
        self.mine_money_price += 10
        
    def add_money(self, amount) :
        self.money += amount
        self.all_money += amount
        
    def remove_money(self, amount) :
        self.money -= amount
        
    def add_token(self) :
        self.token += 1
        
    def add_piece(self) :
        if self.token >= self.pieces_price :
            self.pieces += 1
            self.token -= self.pieces_price
            self.change_piece_price()
            self.state.change_state()
        
    def change_piece_price(self) :
        self.pieces_price += 1
        
    def draw_inventory(self) :
        properties.draw_text(f"money : {self.money}", properties.BLACK, self.money_WIDTH, self.money_HEIGHT)
        properties.draw_text(f"token : {self.token}", properties.BLACK, self.token_WIDTH, self.token_HEIGHT)
        properties.draw_text(f"fuel : {self.fuel}", properties.BLACK, self.fuel_WIDTH, self.fuel_HEIGHT)
        properties.draw_text(f"mine : {self.mine}", properties.BLACK, self.mine_WIDTH, self.mine_HEIGHT)
        properties.draw_text(f"pièces : {self.pieces}, {self.state.state_n}", properties.BLACK, self.pieces_WIDTH, self.pieces_HEIGHT)
