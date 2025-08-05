import pygame
import sys
import random

# Inițializare Pygame
pygame.init()

# Dimensiuni
width = 600
height = 400
block_size = 20

# Culori
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Ecran
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('🐍 Snake Game - Etapa 4')

# Framerate
clock = pygame.time.Clock()
FPS = 10

# Inițializare șarpe și direcție
snake = [(100, 50), (80, 50), (60, 50)]
direction = 'RIGHT'

# Funcție desen șarpe
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], block_size, block_size))

# Funcție generare măr
def generate_apple():
    x = random.randint(0, (width - block_size) // block_size) * block_size
    y = random.randint(0, (height - block_size) // block_size) * block_size
    return (x, y)

# Inițializare măr
apple_pos = generate_apple()

# Funcție Game Over
def game_over():
    font = pygame.font.SysFont('Arial', 36)
    text = font.render('Game Over!', True, WHITE)
    screen.blit(text, (width // 2 - 100, height // 2 - 20))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Buclă principală
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # Mișcare
    x, y = snake[0]
    if direction == 'UP':
        y -= block_size
    elif direction == 'DOWN':
        y += block_size
    elif direction == 'LEFT':
        x -= block_size
    elif direction == 'RIGHT':
        x += block_size

    new_head = (x, y)

    # Coliziune cu pereții
    if x < 0 or x >= width or y < 0 or y >= height:
        game_over()

    # Coliziune cu corpul
    if new_head in snake:
        game_over()

    snake.insert(0, new_head)

    # Mâncare
    if new_head == apple_pos:
        apple_pos = generate_apple()
    else:
        snake.pop()

    # Randare
    screen.fill(BLACK)
    draw_snake(snake)
    pygame.draw.rect(screen, RED, pygame.Rect(apple_pos[0], apple_pos[1], block_size, block_size))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()