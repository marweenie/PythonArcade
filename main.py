#Main file
import pygame

pygame.init()

#hi

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")

fps = pygame.time.Clock()

snake_speed = 15

snake_position = [100, 50]
snake_body = [[100, 50]]

running = True
while running:
# handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0)) #black

    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0),
                         pygame.Rect(pos[0], pos[1], 10, 10))


    pygame.display.update()

pygame.quit()
