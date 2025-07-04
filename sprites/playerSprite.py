import pygame
class Player:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 75
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), (self.x,self.y, self.width,self.height))
        #pygame.draw.rect(screen, (255,255,255), (screen.width,screen.height, self.width,self.height)) # screen height and width?

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= self.speed
        
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += self.speed

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= self.speed
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += self.speed
    def getTile(self,t_width,t_height):
        return (self.x//t_width,self.y//t_height)
        # return tile number in grid type tuple