import math
import numpy as np
#import sys
import pygame
# sys.path.append('..') # add parent directory to path
# from sprites.playerSprite import Player

class Stage:
    def __init__(self,map,collisions,s_width,s_height,t_size,screen):
        self.grid=np.array(map)  # Convert the map to a numpy array for easier slicing
        print(type(self.grid))
        print(type(self.grid[0]))
        print(type(self.grid[0][0]))
        # self.grid=([[0,0,0] for i in range(100)] for j in range(100))
        self.collisions=np.array(collisions)
        self.width=s_width
        self.height=s_height
        self.t_size=t_size
        self.screen=screen
        self.frame_size=(self.width/self.t_size,self.height/self.t_size)

        #pad the grid with null values to account for out of bounds rendering
        print(math.ceil(self.frame_size[0]/2))
        print(math.ceil(self.frame_size[1]/2))
        print(self.grid.shape)

        self.grid=np.pad(
            self.grid,
            ((math.ceil(self.frame_size[1]/2),),(math.ceil(self.frame_size[0]/2),),(0,0)),
            mode='constant',
            constant_values=np.array([0,0,0]))


    def draw(self,player):
        pTile=player.getTile(self.t_size) #get the tile the player is on
        frame=self.grid[ # Defining the frame with numpy slicing breaks at lower bound
            max(pTile[0]-math.ceil(self.frame_size[0]/2),0):min(pTile[0]+math.ceil(self.frame_size[0]/2)+1,len(self.grid[0])),
            max(pTile[1]-math.ceil(self.frame_size[1]/2),0):min(pTile[1]+math.ceil(self.frame_size[1]/2)+1,len(self.grid))      
        ]
        # frame = [[] for i in range(self.frame_size[1])]
        # row_idx = 0
        # for y in range(pTile[1] - math.ceil(self.frame_size[1]/2), pTile[1] + math.ceil(self.frame_size[1]/2)):
        #     for x in range(pTile[0] - math.ceil(self.frame_size[0]/2), pTile[0] + math.ceil(self.frame_size[0]/2)):
        #         # print(len(range(pTile[1] - math.ceil(self.frame_size[1]/2), pTile[1] + math.ceil(self.frame_size[1]/2))))
        #         # print(len(range(pTile[0] - math.ceil(self.frame_size[0]/2), pTile[0] + math.ceil(self.frame_size[0]/2))))
        #         if 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid):
        #             frame[row_idx].append(self.grid[y][x])
        #         else:
        #             frame[row_idx].append((0, 0, 0))
        #     row_idx += 1
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