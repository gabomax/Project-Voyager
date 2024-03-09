import pygame
from properties import Properties

properties = Properties()

class Map() :
    
    def __init__(self) :
        super().__init__()
        self.WIDTH, self.HEIGHT = properties.WIDTH // 8 * 2, properties.HEIGHT // 8 * 4