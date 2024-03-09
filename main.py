import pygame
import pygame_gui
import time
from properties import Properties
from main_screen import MainScreen, State
from game_progress import GameProgress
from shop import Shop
from map import Map
from stage_progress import StageProgress
from inventory import Inventory
from missions import Missions


properties = Properties()
state = State()

pygame.init()

# Initialiser l'écran
mainScreen = MainScreen(state)
gameProgress = GameProgress()
shop = Shop(properties.manager)
map = Map()
stageProgress = StageProgress()
inventory = Inventory(state)
missions = Missions(state, inventory, stageProgress)

properties.add_sprites(mainScreen)
properties.add_sprites(gameProgress)
properties.add_sprites(shop)
properties.add_sprites(map)
properties.add_sprites(stageProgress)
properties.add_sprites(inventory)
properties.add_sprites(missions)

properties.add_item(shop.fuel)
properties.add_item(shop.mine)

money_time = time.time()
clock = pygame.time.Clock()

running = True

while running :
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get() :           
        shop.buy(inventory, event)
        properties.manager.process_events(event)
        
        if event.type == pygame.QUIT :
            running = False
            
    if time.time() - money_time >= 3 :
        inventory.add_money(inventory.mine * 5)
        money_time = time.time()
        
    properties.manager.update(time_delta)
    mainScreen.image = state.state
        
    properties.screen.fill(properties.TURQUOISE)
           
    properties.draw_sprites()
    
    inventory.draw_inventory()
    
    stageProgress.draw_progress()
            
    missions.check_missions()
    missions.show_missions()
    properties.manager.draw_ui(properties.screen)
    
    pygame.display.flip()