# Main file
# Inspired by GeeksForGeeks Snake code snippet: https://www.geeksforgeeks.org/snake-game-in-python-using-pygame-module/
from turtledemo import clock

import pygame
import random

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
fps = 8

def show_score(score):
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
def show_gameover():
    font = pygame.font.SysFont(None, 36)
    gameover_font = pygame.font.SysFont(None, 72)
    gameover_text = gameover_font.render(f"GAME OVER!", True, (255, 0, 0))
    play_again_button_text = font.render(f"Play Again", True, (255, 255, 255))
    quit_button_text = font.render(f"Quit Game", True, (255, 255, 255))
    screen.blit(gameover_text, (137, 175))

    mouse = pygame.mouse.get_pos()
    
    if 230 <= mouse[0] <= 230+144 and 270 <= mouse[1] <= 270+35:
        pygame.draw.rect(screen, (170, 170, 170),
                         pygame.Rect(230, 270, 144, 35))
    else:
        pygame.draw.rect(screen, (100, 100, 100),
                         pygame.Rect(230, 270, 144, 35))
    screen.blit(play_again_button_text, (237, 275))

    if 230 <= mouse[0] <= 230+144 and 330 <= mouse[1] <= 330+35:
        pygame.draw.rect(screen, (170, 170, 170),
                         pygame.Rect(230, 330, 144, 35))
    else:
        pygame.draw.rect(screen, (100, 100, 100),
                         pygame.Rect(230, 330, 144, 35))
    screen.blit(quit_button_text, (237, 335))
    pygame.display.flip()

def main():
    pygame.init()

    blocksize = 20
    direction = 'R'
    change_to = direction
    snake_position = [100, 50]
    snake_body = [[100, 50]]

    fruit_position = [random.randrange(1, (WIDTH // blocksize)) * 10,
                    random.randrange(1, (HEIGHT // blocksize)) * 10]

    fruit_spawn = True
    snake_collision = False
    game_over = False

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
            if(game_over):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 230 <= mouse[0] <= 230+144 and 270 <= mouse[1] <= 270+35:
                        main()
                    if 230 <= mouse[0] <= 230+144 and 330 <= mouse[1] <= 330+35:
                        running = False

        if(not game_over):
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

        mouse = pygame.mouse.get_pos()

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
            game_over = True
            show_gameover()
            # pygame.time.delay(1000)  # ms
            # break
        if snake_position[1] < 0 or snake_position[1] > HEIGHT - 10:
            game_over = True
            show_gameover()
            # pygame.time.delay(1000)
            # break

        for segment in snake_body[1:]:
            if (segment[0] <= fruit_position[0] + 10 and segment[0] >= fruit_position[0] - 10) and (segment[1] <= fruit_position[1] + 10 and segment[1] >= fruit_position[1] - 10):
                fruit_spawn = False
            if snake_position[0] == segment[0] and snake_position[1] == segment[1]:
                # snake_collision = True
                game_over = True
                show_gameover()
                # pygame.time.delay(1000)
                # break

        if snake_collision:
            break

        clock.tick(fps)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()