import math
import numpy as np
import json
import pygame

import random #temp, used to generate random town map colors
RED=(255,0,0) 
GREEN=(0,255,0)
BLUE=(0,0,255)


class Stage:
    def __init__(self,map,collisions,tiles,screen,tile_size,scroll=True):
        self.grid=np.array(map)  # Convert the map to a numpy array for easier slicing
        # self.grid=([0 for i in range(100)] for j in range(100))
        self.collisions=np.array(collisions)
        self.tiles=tiles
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
        #     constant_values=np.array((0,0,0))
        # )


    def draw(self,player):
        pTile=player.getTile(self.tile_size) #get the tile the player is on
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
        print(frame.shape, player.getTile(self.tile_size), (player.x,player.y), sep=' ')
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                pygame.draw.rect(
                    self.screen,
                    frame[i][j],
                    (int((i*self.tile_size) - (int(self.scroll)*(player.x % self.tile_size))),
                    int((j*self.tile_size) - (int(self.scroll)*(player.y % self.tile_size))),
                    self.tile_size,
                    self.tile_size)
                )

def loadMap(filename):
    with open(filename) as f:
        map_data = json.load(f)
        tile_size = map_data['tile_size']
        tiles = map_data['used_tiles']  # This will be a dictionary of tile names to file paths for all tiles used in the map
        grid = map_data['grid']  # This will be a 2D array of tile names used in the map
        grid_collisions = map_data['grid_collisions']  # This will be a 2D array of booleans indicating if a tile is a collision tile
        scroll= map_data['scroll']
    _TOWN=[[(RED,GREEN,BLUE)[random.randint(0,2)] for i in range(100)] for j in range(100)] #generate town map of random tile colors
    _TOWNCOL=[[False for i in range(100)] for j in range(100)]
    return Stage(_TOWN, _TOWNCOL, tiles, pygame.display.get_surface(), tile_size, scroll)
    #return Stage(grid, grid_collisions, width, height, tile_size, scroll)
    

    