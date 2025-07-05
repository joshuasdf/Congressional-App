import math
import numpy as np
import sys
import pygame
sys.path.append('..') # add parent directory to path
from sprites.playerSprite import Player

class Stage:
    def __init__(self,map,collisions,s_width,s_height,t_size,screen):
        self.grid=np.array(map)
        self.collisions=np.array(collisions)
        self.width=s_width
        self.height=s_height
        self.t_size=t_size
        self.screen=screen
    def draw(self,player):
        pTile=player.getTile(self.t_size) #get the tile the player is on
        f_width=math.ceil(self.width/self.t_size) #width of the frame in tiles
        f_height=math.ceil(self.height/self.t_size)# height of the frame in tiles
        frame=self.grid[
            pTile[0]-math.ceil(f_width/2):pTile[0]+math.ceil(f_width/2)+1,
            pTile[1]-math.ceil(f_height/2):pTile[1]+math.ceil(f_height/2)+1
        ] #define the frame of the map visible to the player
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                pygame.draw.rect(
                    self.screen,
                    frame[i][j],
                    (int((i*self.t_size) - (player.x % self.t_size)),
                    int((j*self.t_size) - (player.y % self.t_size)),
                    self.t_size,
                    self.t_size)
                )
                # draw each individual tile at 
                # x=(screen width/2)+(i*tile width)-(player x%tile width)
                # y=(screen height/2)+(i*tile width)-(player x%tile width)