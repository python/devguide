import pygame
import time
import random

# Game window ki settings
window_x = 720
window_y = 480

# Colors define karna
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

pygame.init()
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Snake ki initial position
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]

direction = 'RIGHT'
change_to = direction
score = 0

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: change_to = 'UP'
            if event.key == pygame.K_DOWN: change_to = 'DOWN'
            if event.key == pygame.K_LEFT: change_to = 'LEFT'
            if event.key == pygame.K_RIGHT: change_to = 'RIGHT'

    # Direction change logic
    if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'

    # Snake movement
    if direction == 'UP': snake_position[1] -= 10
    if direction == 'DOWN': snake_position[1] += 10
    if direction == 'LEFT': snake_position[0] -= 10
    if direction == 'RIGHT': snake_position[0] += 10

    # Snake body badhana
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_position = [random.randrange(1, (window_x//10)) * 10,
                          random.randrange(1, (window_y//10)) * 10]
    else:
        snake_body.pop()

    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over logic
    if snake_position[0] < 0 or snake_position[0] > window_x-10 or \
       snake_position[1] < 0 or snake_position[1] > window_y-10:
        pygame.quit()
        quit()

    pygame.display.update()
    fps.tick(15)
