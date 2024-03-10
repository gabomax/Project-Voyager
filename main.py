import pygame
import pygame_gui
import time
from properties import Properties
from main_screen import MainScreen, State
from game_progress import GameProgress
from shop import Shop
from map import Map
from screen_state import ScreenState
from inventory import Inventory
from missions import Missions


properties = Properties()
state = State()
pygame.init()

# Initialiser l'écran
screenState = ScreenState(properties.manager)
mainScreen = MainScreen(state, screenState)
map = Map()
gameProgress = GameProgress()
inventory = Inventory(state)
shop = Shop(properties.manager, gameProgress)
missions = Missions(state, inventory, gameProgress)

properties.add_sprites(mainScreen)
properties.add_sprites(gameProgress)

money_time = time.time()
clock = pygame.time.Clock()

screen = pygame.image.load('assets/screen.png')

running = True

missions.load()
inventory.load()
gameProgress.load()

while running :
    inventory.pieces = state.state_n
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get() :           
        shop.buy(inventory, event)
        screenState.check_button(event)
        properties.manager.process_events(event)
        
        if event.type == pygame.QUIT :
            running = False
            missions.save()
            inventory.save()
            gameProgress.save()
            
    if time.time() - money_time >= 3 :
        inventory.add_money(inventory.mine * 5)
        money_time = time.time()
        
    properties.manager.update(time_delta)
    mainScreen.set_image()
        
    properties.screen.blit(screen, (0, 0))
           
    gameProgress.set_width()
    properties.draw_sprites()
    
    inventory.draw_inventory()
    
    gameProgress.draw_progress()
            
    missions.check_missions()
    missions.show_missions()
    properties.manager.draw_ui(properties.screen)
    screenState.set_image()
    
    pygame.display.flip()