import pygame
# from maps.stage import Stage
class Player:
    def __init__(self, x, y, pWidth, pHeight, FPS):
        self.x = x
        self.y = y
        self.width = pWidth
        self.height = pHeight
        self.speed = 400//FPS
        self.screen = pygame.display.get_surface()

    def draw(self,stage):

        if stage.scroll:
            pygame.draw.rect(
                self.screen,
                (255,255,255),
                (int((self.screen.get_width()-self.width)/2),
                int((self.screen.get_height()-self.height)/2),
                self.width,
                self.height)
            )
            return
        pygame.draw.rect(self.screen, (255,255,255), (self.x,self.y, self.width,self.height))

    def move(self,stage):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed
            if self.checkCollision(stage):
                self.y += self.speed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed
            if self.checkCollision(stage):
                self.y -= self.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed
            if self.checkCollision(stage):
                self.x += self.speed
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed
            if self.checkCollision(stage):
                self.x -= self.speed

    def getTile(self,tile_size):
        return (self.x//tile_size,self.y//tile_size)

    def checkCollision(self, stage):
        stageSize=(len(stage.grid[0])*stage.tile_size,len(stage.grid)*stage.tile_size)
        return(
            stage.collisions[self.getTile(stage.tile_size)[0]-1][self.getTile(stage.tile_size)[1]-1] or
            self.x<0 or
            self.y<0 or
            self.x>stageSize[0] or
            self.y>stageSize[1]
        )