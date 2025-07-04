import pygame
import sys
from sprites.playerSprite import Player
from maps import stage
import random # to test scrolling

pygame.init()

WIDTH, HEIGHT = 1000,750
TILE_WIDTH,TILE_HEIGHT=100,100

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

_TOWN=[[(RED,GREEN,BLUE)[random.randint(0,2)] for i in range(100)] for i in range(100)] #generate town map of random tile colors
stage=stage.Stage(_TOWN,WIDTH,HEIGHT,TILE_WIDTH,TILE_HEIGHT,screen)
player = Player(int((len(_TOWN)*TILE_WIDTH)/2),int(len((_TOWN[0]*TILE_HEIGHT))/2),pWidth,pHeight,screen)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player.move()
    stage.draw(player)
    player.draw()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()