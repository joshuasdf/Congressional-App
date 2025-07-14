import math
import numpy as np
import json
import pygame
import os

import random #temp, used to generate random town map colors
RED=(255,0,0) 
GREEN=(0,255,0)
BLUE=(0,0,255)


class Stage:
    def __init__(self,map,collisions,screen,tile_size,scroll=True):
        self.grid=np.array(map)  # Convert the map to a numpy array for easier slicing
        self.collisions=np.array(collisions)
        self.screen=screen
        self.tile_size=tile_size
        self.frame_size=(self.screen.get_width()/self.tile_size,self.screen.get_height()/self.tile_size)
        self.scroll=scroll

        #pad the grid with null values to account for out of bounds rendering
        print(math.ceil(self.frame_size[0]/2))
        print(math.ceil(self.frame_size[1]/2))
        print(self.grid.shape)

        for i in self.grid:
            print(i.shape)
        # self.grid=np.pad(
        #     self.grid,
        #     ((math.ceil(self.frame_size[1]/2),),(math.ceil(self.frame_size[0]/2),),(0,0)),
        #     mode='constant',
        #     constant_values=None
        # )


    def draw(self,player):
        pTile=player.getTile(self.tile_size) #get the tile the player is on
        frame=self.grid[ # Defining the frame with numpy slicing breaks at lower bound
            max(pTile[0]-math.ceil(self.frame_size[0]/2),0):min(pTile[0]+math.ceil(self.frame_size[0]/2)+1,len(self.grid[0])),
            max(pTile[1]-math.ceil(self.frame_size[1]/2),0):min(pTile[1]+math.ceil(self.frame_size[1]/2)+1,len(self.grid))      
        ]
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                tile_path=frame[i][j]
                tile_rect=(int((i*self.tile_size) - (int(self.scroll)*(player.x % self.tile_size))),
                    int((j*self.tile_size) - (int(self.scroll)*(player.y % self.tile_size))),
                    self.tile_size,
                    self.tile_size)
                if tile_path is not None:
                    # Assuming tile_path is a path to an image file
                    if isinstance(tile_path, str) and os.path.exists(tile_path):
                        image = pygame.image.load(tile_path).convert_alpha()
                        image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
                        self.screen.blit(image,tile_rect)
                        

def loadMap(filename):
    with open(filename) as f:
        map_data = json.load(f)
        tile_size = map_data['tile_size']
        grid = map_data['grid']  # This will be a 2D array of tile names used in the map
        grid_collisions = map_data['grid_collisions']  # This will be a 2D array of booleans indicating if a tile is a collision tile
        scroll= map_data['scroll']
    return Stage(grid, grid_collisions, pygame.display.get_surface(), tile_size, scroll)
    

    