#Main file
#Inspired by GeeksForGeeks Snake code snippet: https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
from turtledemo import clock

import pygame

pygame.init()

#hi

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
fps = 8

blocksize = 20
direction = 'R'
change_to = direction
snake_position = [100, 50]
snake_body = [[100, 50]]

running = True
while running:
# handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "D":
                change_to = 'U'
            elif event.key == pygame.K_DOWN and direction != "U":
                change_to = 'D'
            elif event.key == pygame.K_LEFT and direction != "R":
                change_to = 'L'
            elif event.key == pygame.K_RIGHT and direction != "L":
                change_to = 'R'

    direction = change_to
    if direction == 'U':
        snake_position[1] -= blocksize
    elif direction == 'D':
        snake_position[1] += blocksize
    elif direction == 'L':
        snake_position[0] -= blocksize
    elif direction == 'R':
        snake_position[0] += blocksize

    screen.fill((0,0,0)) #black

    snake_body.insert(0,list(snake_position))
    snake_body.pop()

    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0),
                         pygame.Rect(pos[0], pos[1], blocksize, blocksize))

    if snake_position[0] < 0 or snake_position[0] > WIDTH-10:
        break
    if snake_position[1] < 0 or snake_position[1] > HEIGHT-10:
        break


    clock.tick(fps)
    pygame.display.update()

pygame.quit()
