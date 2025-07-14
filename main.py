import pygame
import sys
import json
from sprites.playerSprite import Player
from maps.stage import *

pygame.init()
pygame.font.init()

ANTI_ALIAS = False

WHITE = (255,255,255)
BLACK = (0,0,0)
RED=(255,0,0) 
GREEN=(0,255,0)
BLUE=(0,0,255)

FPS = 60



#intialize stage and player objects, load map from files
WIDTH=1000
HEIGHT=750

screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.DOUBLEBUF) # doublebuffering to increase visual quality
stage=loadMap("maps/assets/maps/town.json") #at the moment, the map/town.json file is accessed, but its grid is not used to intialize the stage
pWidth = int(WIDTH*0.05)
pHeight = int(HEIGHT*0.075)
player = Player(int((len(stage.grid)*stage.tile_size)/2),int((len(stage.grid[0])*stage.tile_size)/2),pWidth,pHeight, FPS)


pygame.display.set_caption("hello world")

def draw_rect_alpha(color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    s = pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    screen.blit(shape_surf, rect)

    return s

# text stuff
TEXT_SIZE = 32
font = pygame.font.Font("testFont.ttf", TEXT_SIZE)

display_text = True
display_done = False
text_len = 0
text = "hello world"
textevent = pygame.USEREVENT+1
text_surf = font.render(text,True,(255,255,255))
# a timer for the text animation
pygame.time.set_timer(textevent, 200)

# display the text and the background for the text
def display_dialogue():

    bX = 50
    bY = HEIGHT-150
    
    surf = draw_rect_alpha((150, 75, 0, 200), (bX, bY, WIDTH-100, 100))
    return (bX-35, bY+5)

# Main loop
running = True

keys = pygame.key.get_pressed()

clock = pygame.time.Clock()

pygame.event.set_allowed([pygame.KEYDOWN,pygame.QUIT, textevent]) # set the allowed events

while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # the timer event for the text animation
        if event.type == textevent:
            if display_text:
                if not display_done:
                    text_len += 1
                    if text_len > len(text):
                        # text_len = 0
                        display_done = True

                    if text_len == 0:
                        text_surf = font.render(text,True,(255,255,255))
                    else:
                        text_surf = font.render(text[:text_len], True, (255, 255, 255))


        if event.type == pygame.MOUSEBUTTONDOWN:
            # checks if the text is done displaying
            if display_done:
                display_text = False

    player.move(stage)
    stage.draw(player)
    player.draw(stage)

    # display the text
    if display_text:
        surf = display_dialogue()
        screen.blit(text_surf, text_surf.get_rect(topleft = surf).move(40, 0))


    pygame.display.flip()

pygame.quit()
sys.exit()