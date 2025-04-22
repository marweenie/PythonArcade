# Main file
# Inspired by GeeksForGeeks Snake code snippet: https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
from turtledemo import clock

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
fps = 8
font = pygame.font.SysFont(None, 36)
gameover_font = pygame.font.SysFont(None, 72)

def show_score(score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
def show_gameover():
    gameover_text = gameover_font.render(f"GAME OVER!", True, (255, 0, 0))
    screen.blit(gameover_text, (137, 175))
    pygame.display.flip()

blocksize = 20
direction = 'R'
change_to = direction
snake_position = [100, 50]
snake_body = [[100, 50]]

fruit_position = [random.randrange(1, (WIDTH // blocksize)) * 10,
                  random.randrange(1, (HEIGHT // blocksize)) * 10]

fruit_spawn = True
snake_collision = False

score = 0

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

    ate_fruit = False
    if (snake_position[0] <= fruit_position[0] + 10 and snake_position[0] >= fruit_position[0] - 10) and (
            snake_position[1] <= fruit_position[1] + 10 and snake_position[1] >= fruit_position[1] - 10):
        score += 1
        fruit_spawn = False
        ate_fruit = True

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WIDTH // blocksize)) * 10,
                          random.randrange(1, (HEIGHT // blocksize)) * 10]

    fruit_spawn = True

    screen.fill((0, 0, 0))  # black

    snake_body.insert(0, list(snake_position))
    if not ate_fruit:
        snake_body.pop()

    for pos in snake_body:
        pygame.draw.rect(screen, (0, 255, 0),
                         pygame.Rect(pos[0], pos[1], blocksize, blocksize))

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
        fruit_position[0], fruit_position[1], blocksize, blocksize))
    
    show_score(score)

    if snake_position[0] < 0 or snake_position[0] > WIDTH - 10:
        show_gameover()
        pygame.time.delay(1000)  # ms
        break
    if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
        show_gameover()
        pygame.time.delay(1000)
        break

    for segment in snake_body[1:]:
        if (segment[0] <= fruit_position[0] + 10 and segment[0] >= fruit_position[0] - 10) and (segment[1] <= fruit_position[1] + 10 and segment[1] >= fruit_position[1] - 10):
            fruit_spawn = False
        if snake_position[0] == segment[0] and snake_position[1] == segment[1]:
            snake_collision = True
            show_gameover()
            pygame.time.delay(1000)
            break

    if snake_collision:
        break

    clock.tick(fps)
    pygame.display.update()

pygame.quit()
