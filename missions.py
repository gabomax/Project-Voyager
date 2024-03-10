import pygame
import pickle
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
        self.mission1_WIDTH, self.mission1_HEIGHT = properties.WIDTH // 8 * 7 - 115, properties.HEIGHT // 8 * 5 + 27
        
        self.mission2 = False
        self.mission2_fuel = 1000
        self.mission2_WIDTH, self.mission2_HEIGHT = properties.WIDTH // 8 * 7 - 115, properties.HEIGHT // 8 * 6 + 15
        
        self.mission3 = False
        self.mission3_mine = 50
        self.mission3_WIDTH, self.mission3_HEIGHT = properties.WIDTH // 8 * 7 - 115, properties.HEIGHT // 8 * 7 
            
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
            
    def save_mission1_bool(self) :
        with open('mission1_bool.pickle', 'wb') as f:
            pickle.dump(self.mission1, f)
            
    def load_mission1_bool(self):
        try:
            with open('mission1_bool.pickle', 'rb') as f:
                self.mission1 = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mission1 = False
            
    def save_mission1(self) :
        with open('mission1.pickle', 'wb') as f:
            pickle.dump(self.mission1_money, f)
            
    def load_mission1(self):
        try:
            with open('mission1.pickle', 'rb') as f:
                self.mission1_money = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mission1_money = 100
            
    def save_mission2_bool(self) :
        with open('mission2_bool.pickle', 'wb') as f:
            pickle.dump(self.mission2, f)
            
    def load_mission2_bool(self):
        try:
            with open('mission2_bool.pickle', 'rb') as f:
                self.mission2 = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mission2 = False
            
    def save_mission2(self) :
        with open('mission2.pickle', 'wb') as f:
            pickle.dump(self.mission2_fuel, f)
            
    def load_mission2(self):
        try:
            with open('mission2.pickle', 'rb') as f:
                self.mission2_fuel = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mission2_fuel = 1000
            
    def save_mission3_bool(self) :
        with open('mission3_bool.pickle', 'wb') as f:
            pickle.dump(self.mission3, f)
            
    def load_mission3_bool(self):
        try:
            with open('mission3_bool.pickle', 'rb') as f:
                self.mission3 = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mission3 = False
            
    def save_mission3(self) :
        with open('mission3.pickle', 'wb') as f:
            pickle.dump(self.mission3_mine, f)
            
    def load_mission3(self):
        try:
            with open('mission3.pickle', 'rb') as f:
                self.mission3_mine = pickle.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas encore, retourne 0 comme argent par défaut
            self.mission3_mine = 50
            
    def save(self) :
        self.save_mission1_bool()
        self.save_mission1()
        
        self.save_mission2_bool()
        self.save_mission2()
        
        self.save_mission3_bool()
        self.save_mission3()
            
    def load(self) :
        self.load_mission1_bool()
        self.load_mission1()
        
        self.load_mission2_bool()
        self.load_mission2()
        
        self.load_mission3_bool()
        self.load_mission3()
    