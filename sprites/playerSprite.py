import pygame
class Player:
    def __init__(self, x, y, pWidth, pHeight, screen):
        self.x = x
        self.y = y
        self.width = pWidth
        self.height = pHeight
        self.speed = 5
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), (self.x,self.y, self.width,self.height))

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