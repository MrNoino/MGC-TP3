import pygame, sys
from pygame.locals import *
import random, time
from player import Player
from npc import Enemy
import utils
from globals import *
from _thread import *
from cliente import Network

pygame.init()

menu_font = pygame.font.Font(None, 50)
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 18)
font_micro = pygame.font.SysFont("Verdana", 10)

DISPLAY = pygame.display.get_desktop_sizes()[0]
DISPLAY = (DISPLAY[0], DISPLAY[1]-50)

#DISPLAYSURF = pygame.display.set_mode(DISPLAY)
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.RESIZABLE, vsync=1)

def initGraphics(DS):
    
    DS.fill(WHITE)

    item_surface = font.render("Bem-Vindo ao Zombie Party!", True, GRAY)

    item_rect = item_surface.get_rect(center=(DISPLAY[0]// 2, DISPLAY[1] // 2))

    DS.blit(item_surface, item_rect)

    pygame.display.flip()

    time.sleep(1)

    game_menu(['Iniciar jogo', 'Sair'])

def graphics(DS, background, score, score_per_kill, waves, shots):
    for y in range(5):

            for x in range(10):

                location = (x * background.get_width(), y * background.get_height())

                DISPLAYSURF.blit(background, location)

    pygame.draw.rect(DISPLAYSURF, WHITE_GRAY,(0, 0, DISPLAY[0], 30),15, border_radius=0)

    DISPLAYSURF.blit(font_micro.render("Pontuação: ", True, GRAY), (30, 8))

    DISPLAYSURF.blit(font_small.render(str(score), True, BLACK), (100, 3))

    DISPLAYSURF.blit(font_micro.render("Pontos por morte: ", True, GRAY), ((DISPLAY[0] // 3) -100, 8))

    DISPLAYSURF.blit(font_small.render(str(score_per_kill), True, BLACK), ((DISPLAY[0]/3), 3))

    DISPLAYSURF.blit(font_micro.render("Ordas: ", True, GRAY), (DISPLAY[0]-80, 8))

    DISPLAYSURF.blit(font_small.render(str(waves), True, BLACK), (DISPLAY[0] -30, 3))

    DISPLAYSURF.blit(font_micro.render("Tiros: ", True, GRAY), (int(DISPLAY[0]/2), 8))

    try:

        bullet_image = pygame.image.load("png/Objects/Bullet_002.png")

    except Exception as e:

        #escreve um log com a exceção
        utils.saveLog(e)

        exit()

    for i in range(shots):

        DISPLAYSURF.blit(pygame.transform.smoothscale(bullet_image, (20,16)), (int(DISPLAY[0]/2)+30+20*i, 7))

def game_menu(menu_items):

    # Título da janela do jogo
    pygame.display.set_caption("Menu de jogo")

    pygame.event.clear()

    selected_item = 0

    # Loop do menu
    while True:
        # Desenhar o fundo do menu
        DISPLAYSURF.fill(WHITE)

        item_surface = font.render("Zombie Party", True, YELLOW)
        item_rect = item_surface.get_rect(center=(DISPLAY[0] // 2, 200))
        DISPLAYSURF.blit(item_surface, item_rect)

        # Desenhar os itens do menu
        for index, item in enumerate(menu_items):
            # Desenhar o item
            item_surface = menu_font.render(item, True, BLACK)
            item_rect = item_surface.get_rect(center=(DISPLAY[0]// 2, DISPLAY[1] // 2 + index * 50))
            DISPLAYSURF.blit(item_surface, item_rect)

            # Desenhar um indicador de seleção ao redor do item selecionado
            if index == selected_item:
                pygame.draw.rect(DISPLAYSURF, BLACK, item_rect.inflate(20, 20), 3)

        item_surface = font_small.render("Nuno Lopes", True, BLACK)
        item_rect = item_surface.get_rect(center=(DISPLAY[0]//2, DISPLAY[1] -40))
        DISPLAYSURF.blit(item_surface, item_rect)

        item_surface = font_small.render("Karine Florêncio", True, BLACK)
        item_rect = item_surface.get_rect(center=(DISPLAY[0]//2, DISPLAY[1] -20))
        DISPLAYSURF.blit(item_surface, item_rect)

        # Atualizar a tela
        pygame.display.flip()

        # Verificar os eventos do menu
        for event in pygame.event.get():
            # Verificar se o usuário fechou a janela
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Verificar se o usuário pressionou uma tecla
            elif event.type == pygame.KEYDOWN:
                # Verificar se a tecla pressionada foi para cima ou para baixo
                if event.key == pygame.K_UP:
                    # Selecionar o item anterior
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    # Selecionar o próximo item
                    selected_item = (selected_item + 1) % len(menu_items)
                # Verificar se a tecla pressionada foi Enter
                elif event.key == pygame.K_RETURN or event.key == pygame.KSCAN_RETURN:
                    # Executar a ação do item selecionado
                    if menu_items[selected_item] == 'Iniciar jogo' or menu_items[selected_item] == 'Recomeçar jogo':
                        
                        game()

                    elif menu_items[selected_item] == 'Continuar jogo':

                        return

                    elif menu_items[selected_item] == 'Sair':
                        pygame.quit()
                        sys.exit()

def final(DS, msg, color, score, waves, all_sprites, all_shots):

    DS.fill(WHITE)

    item_surface = font.render(msg, True, color)

    item_rect = item_surface.get_rect(center=(DISPLAY[0]// 2, DISPLAY[1] // 2))

    DS.blit(item_surface, item_rect)

    item_surface = font_small.render("Pontuação: " + str(score), True, BLUE)

    item_rect = item_surface.get_rect(center=(DISPLAY[0]// 2, (DISPLAY[1] // 2) +50))

    DS.blit(item_surface, item_rect)

    item_surface = font_small.render("Ordas concluídas: " + str(waves), True, BLUE)

    item_rect = item_surface.get_rect(center=(DISPLAY[0]// 2, (DISPLAY[1] // 2) +70))

    DS.blit(item_surface, item_rect)

    for entity in all_sprites:

        entity.kill()

    for shot in all_shots:

        shot.kill()

    pygame.display.flip()

    time.sleep(5)

    game_menu(['Recomeçar jogo', 'Sair'])


aux_npcs = None

def generateNPCS(waves, interval):

    numberNPCS = waves * random.randint(interval[0], interval[1])

    global aux_npcs
    npcs = []

    for i in range(numberNPCS):

        npcs.append(Enemy((DISPLAY[0] + (i+1) * random.randint(60, 80), random.randint(80, DISPLAY[1] -55))))

    aux_npcs = npcs

def game():

    try:

        background =  pygame.transform.smoothscale(pygame.image.load("png/grass-hanpaited2.jpg"),(200,200))

    except Exception as e:

        #escreve um log com a exceção
        utils.saveLog(e)

        exit()

    pygame.display.set_caption("Zombie Party")

    P1 = Player("P1", 'F', (50, random.randint(80,DISPLAY[1] -55)))

    players = pygame.sprite.Group()
    players.add(P1)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)

    waves = 1

    npc_speed = 1

    score_per_kill = 50

    generateNPCS(waves, (2, 5))

    global aux_npcs

    npcs = aux_npcs

    aux_npcs = None

    all_sprites.add(npcs)

    enemies = pygame.sprite.Group()

    enemies.add(npcs)

    all_shots = pygame.sprite.Group()

    deads = pygame.sprite.Group()

    clock = pygame.time.Clock()

    thread = False

    shotZumbi = None
    
    while True:

        clock.tick(30)

        graphics(DISPLAYSURF, background, P1.getScore(), score_per_kill, waves, 10-len(all_shots))

        for npc in enemies:

            npc.move(DISPLAY, npc_speed)

        P1.move(DISPLAY)

        P1.shoot(DISPLAY, all_shots)

        for shot in all_shots:

            shot.move(DISPLAY, shot_speed)

            shot.draw(DISPLAYSURF)

        for i in all_sprites:

            i.draw(DISPLAYSURF)
          
        for i in deads:
            final_p = i.animatedead()
            i.draw(DISPLAYSURF)

            if final_p:
                final(DISPLAYSURF, "GAME OVER!", RED, P1.getScore(), waves-1, all_sprites, all_shots)


        if len(enemies) == 0:

            pygame.display.update()

            if not thread:

                waves +=1
            
                npc_speed *= 1.25

                score_per_kill *= 2

                start_new_thread(generateNPCS, (waves, (2, 5)))

                thread = True
            
            if aux_npcs:

                npcs = aux_npcs

                all_sprites.add(npcs)

                enemies.add(npcs)

                aux_npcs = None

                thread = False

            continue

        for npc in enemies:

            if npc.getFinal(DISPLAY):

                final(DISPLAYSURF, "GAME OVER!", RED, P1.getScore(), waves-1, all_sprites, all_shots)

        collide = pygame.sprite.groupcollide(players, enemies, True , True)

        if collide:
            item = collide.popitem()
            player = item[0]
            enemy = item[1][0]
            enemy.setPosition(enemy.getPosition())
            player.notMove()
            deads.add(player)
            deads.add(enemy)

           
        shotZumbi = pygame.sprite.groupcollide(all_shots, enemies, True ,True)

        if shotZumbi:
            item = shotZumbi.popitem()
            shot_at = item[0]
            at_npc = item[1][0]
            at_npc.setPosition(at_npc.getPosition())
            shot_at.setPosition(at_npc.rect.bottomleft)
            deads.add(shot_at)
            deads.add(at_npc)
            P1.incrementScore(score_per_kill)


        for event in pygame.event.get():

            if event.type == QUIT:

                pygame.quit()

                sys.exit()

        __pressed_keys = pygame.key.get_pressed()
        if __pressed_keys[K_ESCAPE]:

                game_menu(["Continuar jogo", "Sair"])

        
        pygame.display.update()
        


# while True:

#     name = input("Please enter your name: ")

#     if  0 < len(name) < 35:
#         break
#     else:
#         print("Erro: Quantidade de caracteres inaceitável.")

# while(True):
#     # print("'C' - Comboy or 'R' - Robot")
#     skin = input("'C' - Cowboy or 'R' - Robot\nEscolha sua skin: ")

#     if skin in ['R','C','r','c']:
#         break
#     else:
#         print("Erro: Valor inválido.")

# if skin in ['R','r']:
#     skin = 'M'
# else:
#     skin = 'F'

# connection_server = Network()
# current_id = connection_server.connect(name,skin)
# info_game = connection_server.send("get")

# alterar dados do game com ^^^^^^

initGraphics(DISPLAYSURF)