import pygame
width = 800
height = 800
pygame.init()
clock = pygame.time.Clock()
screen=pygame.display.set_mode((width,height))
surface = pygame.Surface((width,height), pygame.SRCALPHA)

while True:
    msElapsed = clock.tick(100)
    screen.fill((0,0,0,255))
    pygame.draw.circle(surface,(30,224,33,100),(250,100),10)
    screen.blit(surface, (0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()