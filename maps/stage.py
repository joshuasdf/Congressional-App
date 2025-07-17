import math
import numpy as np
import json
import pygame
import os

RED=(255,0,0) 
GREEN=(0,255,0)
BLUE=(0,0,255)


class Stage:
    def __init__(self,map,collisions,used_tiles,screen,tile_size,scroll=True):
        self.grid=np.array(map)  # Convert the map to a numpy array for easier slicing
        self.collisions=np.array(collisions)
        self.screen=screen
        self.tile_size=tile_size
        self.scroll=scroll
        self.used_tiles=used_tiles  # cache of images used in the stage, to avoid loading the same image multiple times
        #pad the grid with null values to account for out of bounds rendering

        #aux attributes for rendering
        self.frame_size=(self.screen.get_width()/self.tile_size,self.screen.get_height()/self.tile_size)
        self.pad_height, self.pad_width=math.ceil(self.frame_size[1]/2),math.ceil(self.frame_size[0]/2)
        self.padded_grid=np.pad(
            self.grid,
            ((self.pad_height,),(self.pad_width,)),
            mode='constant',
            constant_values=None
        )


    def draw(self,player):
        pTile=player.getTile(self.tile_size) #get the tile the player is on
        frame=self.padded_grid[ # Defining the frame with numpy slicing breaks at lower bound
            # max(pTile[0]-math.ceil(self.frame_size[0]/2),0):min(pTile[0]+math.ceil(self.frame_size[0]/2)+1,len(self.grid[0])),
            # max(pTile[1]-math.ceil(self.frame_size[1]/2),0):min(pTile[1]+math.ceil(self.frame_size[1]/2)+1,len(self.grid))
            pTile[1]:pTile[1]+2*self.pad_height+1,   
            pTile[0]:pTile[0]+2*self.pad_width+1
        ]
        print(self.pad_width,self.pad_height,frame.shape,end=' ')
        for j in range(len(frame)):
            for i in range(len(frame[0])):
                tile_path=frame[j][i] #i is rows, j is columns
                tile_rect=(int((i*self.tile_size) - (int(self.scroll)*(player.x % self.tile_size))),
                    int((j*self.tile_size) - (int(self.scroll)*(player.y % self.tile_size))),
                    self.tile_size,
                    self.tile_size)
                if tile_path is not None:
                    if isinstance(tile_path, str) and os.path.exists(tile_path):
                        image = self.used_tiles[tile_path]
                        image = pygame.transform.scale(image, (self.tile_size, self.tile_size))
                        self.screen.blit(image,tile_rect)
                        

def loadMap(filename):
    with open(filename) as f:
        map_data = json.load(f)
        tile_size = map_data['tile_size']
        grid = map_data['grid']  # This will be a 2D array of tile names used in the map
        grid_collisions = map_data['grid_collisions']  # This will be a 2D array of booleans indicating if a tile is a collision tile
        scroll= map_data['scroll']
        used_tiles = {tile: pygame.image.load(tile).convert_alpha() for tile in map_data.get('used_tiles', []) if os.path.exists(tile)}
    return Stage(grid, grid_collisions, used_tiles, pygame.display.get_surface(), tile_size, scroll)
    

    