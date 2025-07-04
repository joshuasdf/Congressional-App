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

pWidth = WIDTH*0.05
pHeight = HEIGHT*0.075

player = Player(0,0,pWidth,pHeight,screen)

_TOWN=[[(RED,GREEN,BLUE)[random.randint(0,2)] for i in range(100)] for i in range(100)] #generate town map of random tile colors
stage=stage.Stage(_TOWN,WIDTH,HEIGHT,TILE_WIDTH,TILE_HEIGHT)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player.draw()
    player.move()
    player.move()
    stage.draw(screen, player)
    player.draw(screen)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()