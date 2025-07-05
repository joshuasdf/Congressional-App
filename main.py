import pygame
import sys
import json
from sprites.playerSprite import Player
from maps import stage
import random # to test scrolling

pygame.init()

with open("maps/town.json") as f:
    town_data = json.load(f)#currently, all of the values in the grid and grid collisions are placeholders
    WIDTH, HEIGHT = town_data['width'], town_data['height']
    TILE_SIZE = town_data['tile_size']
    TILES= town_data['used_tiles']  # This will be a dictionary of tile names to file paths for all tiles used in the map
    GRID = town_data['grid']  # This will be a 2D array of tile names used in the map
    GRID_COLLISIONS = town_data['grid_collisions']  # This will be a 2D array of booleans indicating if a tile is a collision tile
    #later, once we have tiles built into the json file, the stage will be initialized here with the town_data


WHITE = (255,255,255)
BLACK = (0,0,0)

RED=(255,0,0) 
GREEN=(0,255,0)
BLUE=(0,0,255)

FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True

keys = pygame.key.get_pressed()

clock = pygame.time.Clock()

pWidth = int(WIDTH*0.05)
pHeight = int(HEIGHT*0.075)

_TOWN=[[(RED,GREEN,BLUE)[random.randint(0,2)] for i in range(100)] for j in range(100)] #generate town map of random tile colors
_TOWNCOL=[[False for i in range(100)] for j in range(100)]
stage=stage.Stage(_TOWN,_TOWNCOL,WIDTH,HEIGHT,TILE_SIZE,screen)
player = Player(int((len(_TOWN)*TILE_SIZE)/2),int(len((_TOWN[0]*TILE_SIZE))/2),pWidth,pHeight,screen)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player.move(stage)
    stage.draw(player)
    player.draw()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()