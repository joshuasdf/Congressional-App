from sprites.playerSprite import Player
import math

class Stage:
    def __init__(self,map,s_width,s_height,t_width,t_height):
        self.grid=map
        self.width=s_width
        self.height=s_height
        self.t_width=t_width
        self.t_height=t_height
    def draw(self,screen,player):
        pTile=player.getTile
        f_width=math.ceil(self.width/self.t_width) #width of the frame in tiles
        f_height=math.ceil(self.height/self.t_height)# height of the fram in tiles
        frame=self.grid[
            pTile[0]-math.ceil(f_width/2):pTile[0]+math.ceil(f_width/2)
            ][
            pTile[1]-math.ceil(f_height/2):pTile[1]+math.ceil(f_height/2)
        ] #define the frame of the map visible to the player
        for i in range(len(frame)):
            for j in range(len(frame[0])):
                pass
                # draw each individual tile at 
                # x=(screen width/2)+(i*tile width)-(player x%tile width)
                # y=(screen height/2)+(i*tile width)-(player x%tile width)