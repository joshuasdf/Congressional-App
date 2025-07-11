import pygame
import sys
import json
from sprites.playerSprite import Player
from maps import stage
import random # to test scrolling

pygame.init()
pygame.font.init()


with open("maps/town.json") as f:
    town_data = json.load(f)#currently, all of the values in the grid and grid collisions are placeholders
    WIDTH, HEIGHT = town_data['width'], town_data['height']
    TILE_SIZE = town_data['tile_size']
    TILES= town_data['used_tiles']  # This will be a dictionary of tile names to file paths for all tiles used in the map
    GRID = town_data['grid']  # This will be a 2D array of tile names used in the map
    GRID_COLLISIONS = town_data['grid_collisions']  # This will be a 2D array of booleans indicating if a tile is a collision tile
    #later, once we have tiles built into the json file, the stage will be initialized here with the town_data


ANTI_ALIAS = False

WHITE = (255,255,255)
BLACK = (0,0,0)

RED=(255,0,0) 
GREEN=(0,255,0)
BLUE=(0,0,255)

FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT), pygame.DOUBLEBUF) # doublebuffering to increase visual quality
pygame.display.set_caption("hello world")


running = True

keys = pygame.key.get_pressed()

clock = pygame.time.Clock()

pWidth = int(WIDTH*0.05)
pHeight = int(HEIGHT*0.075)

_TOWN=[[(RED,GREEN,BLUE)[random.randint(0,2)] for i in range(100)] for j in range(100)] #generate town map of random tile colors
_TOWNCOL=[[False for i in range(100)] for j in range(100)]
stage=stage.Stage(_TOWN,_TOWNCOL,WIDTH,HEIGHT,TILE_SIZE,screen,scroll=True)
player = Player(int((len(_TOWN)*TILE_SIZE)/2),int(len((_TOWN[0]*TILE_SIZE))/2),pWidth,pHeight,screen, FPS)


# draw a translucent rectangle
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

    stage.draw(player)

    player.move(stage)
    player.draw(stage)


    # display the text
    if display_text:
        surf = display_dialogue()
        screen.blit(text_surf, text_surf.get_rect(topleft = surf).move(40, 0))


    pygame.display.flip()

pygame.quit()
sys.exit()