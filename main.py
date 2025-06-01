import pygame

pygame.init()

WIDTH, HEIGHT = 1000,750

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

running = True

keys = pygame.key.get_pressed()

clock = pygame.time.Clock()

class Player:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.width = WIDTH*0.05
        self.height = HEIGHT*0.075
        self.speed = 5

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x,self.y, self.width,self.height))

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

player = Player(0,0)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player.draw()
    player.move()
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
exit()