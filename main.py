#Main file
import pygame

pygame.init()

#hi

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

snake_position = [100, 50]
snake_body = [[100, 50]]

running = True
while running:
    screen.fill((0,0,0)) #black

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()

pygame.quit()
