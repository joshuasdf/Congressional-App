import pygame
import sys
from sprites.playerSprite import Player

pygame.init()

WIDTH, HEIGHT = 1000,750

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True

keys = pygame.key.get_pressed()

clock = pygame.time.Clock()

pWidth = WIDTH*0.05
pHeight = HEIGHT*0.075

player = Player(0,0,pWidth,pHeight,screen)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player.draw()
    player.move()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()