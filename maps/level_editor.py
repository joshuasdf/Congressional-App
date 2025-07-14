import pygame
import json
import os
import random

level_path = "maps/assets/maps/town.json"

class Editor:
    def __init__(self, level, screen):
        with open(level, 'r') as f:
            map_data = json.load(f)
            self.tile_size = map_data['tile_size']
            self.level=map_data['name']
        self.screen = screen
        self.width=screen.get_width()/2
        self.height=screen.get_height()
        self.surface=pygame.Surface((self.width, self.height))


class Builder(Editor):
    def __init__(self, level, screen):
        super().__init__(level, screen)
        with open(level, 'r') as f:
            map_data = json.load(f)
            self.grid = map_data['grid']  # This will be a 2D array of tile names used in the map
            self.collisions = map_data['grid_collisions']
            self.scroll = map_data['scroll']

class Palette(Editor):
    def __init__(self, level, screen):
        super().__init__(level, screen)
        with open(level, 'r') as f:
            map_data = json.load(f)
            self.grid = map_data['grid']  # set this to a list of all tiles in the tiles directory
        self.brush= None  # This will be set to the tile currently selected in the palette


def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 750), pygame.DOUBLEBUF)
    builder = Builder(level_path,screen)
    palette = Palette(level_path, screen)

    # main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((0, 0, 0))  # Clear the screen with black
        
        # get mouse position

        #if  mouse is on the left half of the screen:
        # builder.move
        # builder tick (edit the map if mouse down)
        # builder.draw
        #
        #if mouse is on the right half of the screen:
        # palette.move
        # palette tick (select tile for brush if mouse down)
        # palette.draw

        # blit builder surface on the left half of the screen
        # blit the palette surface on the right half of the screen

        pygame.display.flip()  # Update the display



    with open(level_path, 'w') as f: # save changes to the map file
        tiles=list(set([tile for row in builder.grid for tile in row if tile is not None]))
        print(tiles)
        map_data = {
            "name": builder.level,
            "tile_size": builder.tile_size,
            "used_tiles": tiles,
            "scroll": builder.scroll,
            "grid": builder.grid,
#            "grid": [[("maps/assets/tiles/dirt.png","maps/assets/tiles/water1.png","maps/assets/tiles/grass.png")[random.randint(0,2)] for i in range(100)] for j in range(100)],
            "grid_collisions": builder.collisions
        }
        json.dump(map_data, f, indent=4)    




if __name__ == "__main__":
    main()