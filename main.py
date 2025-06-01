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

player = Player(0,0)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player.draw(screen)
    player.move()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()