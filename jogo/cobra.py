import pygame
import random
import time
import sys
 
# Define algumas cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Inicializa o Pygame
pygame.init()

# Define as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Define o título da janela
pygame.display.set_caption('Jogo da Cobra')
 
# Define a taxa de atualização da tela
clock = pygame.time.Clock()

# Variáveis do jogo
snake_position = [100,100]
snake_body = [[100,100],[90,100],[80,100]]
food_position = [300,300]
food_spawn = True
 
direction = 'RIGHT'
change_to = direction
 
score = 0
 
# Cria uma fonte para exibir o placar
font = pygame.font.Font('freesansbold.ttf', 18)
 
# Define o placar inicial
def show_score(choice, color, font, size, x, y):
    score_font = pygame.font.Font(font, size)
    score_surface = score_font.render(str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (x, y)
    elif choice == 2:
        score_rect.midbottom = (x, y)
    screen.blit(score_surface, score_rect)
     
# Game Over
def game_over():
    my_font = pygame.font.Font('freesansbold.ttf', 72)
    game_over_surface = my_font.render('Fim de jogo', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width/2, screen_height/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

# Controla a velocidade do jogo
speed = 15
 
# Executa o jogo
while True:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    # Verifica se a cobra colidiu com a borda
    if snake_position[0] > screen_width or snake_position[0] < 0:
        game_over()
    if snake_position[1] > screen_height or snake_position[1] < 0:
        game_over()
         
    # Verifica se a cobra colidiu consigo mesma
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()
 
    # Faz a cobra se mover
    if change_to == 'UP':
        snake_position[1] -= 10
    if change_to == 'DOWN':
        snake_position[1] += 10
    if change_to == 'LEFT':
        snake_position[0] -= 10
    if change_to == 'RIGHT':
        snake_position[0] += 10
 
    # Faz a comida aparecer aleatoriamente na tela
    if food_spawn == False:
        food_position = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True
 
    # Cria uma nova cabeça para a cobra
    snake_body.insert(0, list(snake_position))
 
    # Verifica se a cobra comeu a comida
    if snake_position == food_position:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
         
    # Desenha a tela
    screen.fill(BLACK)
     
    # Desenha a comida
    pygame.draw.rect(screen, WHITE, pygame.Rect(food_position[0], food_position[1], 10, 10))
     
    # Desenha a cobra
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
     
    # Atualiza o placar
    show_score(1, WHITE, 'freesansbold.ttf', 20, screen_width/2, 10)
     
    # Atualiza a tela
    pygame.display.update()
     
    # Define a velocidade do jogo
    clock.tick(speed)