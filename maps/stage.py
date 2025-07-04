import math
import numpy as np
import sys
import pygame
sys.path.append('..') # add parent directory to path
from sprites.playerSprite import Player

class Stage:
    def __init__(self,map,s_width,s_height,t_width,t_height,screen):
        self.grid=np.array(map)
        self.width=s_width
        self.height=s_height
        self.t_width=t_width
        self.t_height=t_height
        self.screen=screen
    def draw(self,player):
        pTile=player.getTile(self.t_width,self.t_height) #get the tile the player is on
        print(f"Player Tile: {pTile}")
        f_width=math.ceil(self.width/self.t_width) #width of the frame in tiles
        f_height=math.ceil(self.height/self.t_height)# height of the fram in tiles
        print(f"Frame Width: {f_width}, Frame Height: {f_height}")
        print(pTile[0]-math.ceil(f_width/2), pTile[0]+math.ceil(f_width/2),
              pTile[1]-math.ceil(f_height/2), pTile[1]+math.ceil(f_height/2))
        frame=self.grid[
            pTile[0]-math.ceil(f_width/2):pTile[0]+math.ceil(f_width/2)+1,
            pTile[1]-math.ceil(f_height/2):pTile[1]+math.ceil(f_height/2)+1
        ] #define the frame of the map visible to the player
        print(f"Frame: {frame}")
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                pygame.draw.rect(
                    self.screen,
                    frame[i][j],
                    (int((i*self.t_width) - (player.x % self.t_width)),
                    int((j*self.t_height) - (player.y % self.t_height)),
                    self.t_width,
                    self.t_height)
                )
                # draw each individual tile at 
                # x=(screen width/2)+(i*tile width)-(player x%tile width)
                # y=(screen height/2)+(i*tile width)-(player x%tile width)