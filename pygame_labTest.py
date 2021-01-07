import pygame


width, height = 800, 800
rows, cols = 8, 8
sqsize = width // cols
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
fps = 60

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    pygame.quit()


main()
