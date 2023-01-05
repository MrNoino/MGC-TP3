import pygame, sys
from pygame.locals import *
import random, time
from player import Player
from entity import Entity
from npc import Enemy
import shot
import utils
from globals import *

SPEED = 1

try:

    player_img = pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Idle (1).png"), player_size)

except Exception as e:

    #escreve um log com a exceção
    utils.saveLog(e)

    exit(1)


#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (120, 255, 120)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)

def initGraphics(DS):
    #pygame.mixer.Sound('background.wav').play(loops=-1)
    DS.fill(WHITE)
    global font_small
    DS.blit(font_small.render("Bem-Vindo ao Zgame!",True,BLUE), (50,50))
    pygame.display.flip()
    time.sleep(1)

def gameOver(DS, all_sprites, all_shots):
    DS.fill(RED)
    # gameOver(DISPLAYSURF) a criar...
    event = pygame.event.wait()
    pressed_key = pygame.key.get_pressed()
    if event.type == KEYDOWN:
        if pressed_key[K_r]:
            # setupGame(DISPLAYSURF)
            1==1
        if pressed_key[K_e]:
            for entity in all_sprites:
                entity.kill()
            for shot in all_shots:
                shot.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()

#Initialzing
pygame.init()
# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

DISPLAY = pygame.display.get_desktop_sizes()[0]
DISPLAY = (DISPLAY[0], DISPLAY[1]-50)

try:

    background =  pygame.transform.smoothscale(pygame.image.load("png/grass-hanpaited2.jpg"),(200,200))

except Exception as e:

    #escreve um log com a exceção
    utils.saveLog(e)

    exit


#Create a white screen
DISPLAYSURF = pygame.display.set_mode(DISPLAY)
#DISPLAYSURF.fill(WHITE)

pygame.display.set_caption("Zgame")
P1 = Player("P1", player_img, (50, DISPLAY[1]/2))
E1 = Enemy((DISPLAY[0], random.randint(5,DISPLAY[1]-25)))
E2 = Enemy((DISPLAY[0], random.randint(5,DISPLAY[1]-25)))

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)

enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)

all_shots = pygame.sprite.Group()

initGraphics(DISPLAYSURF)
#pygame.mixer.Sound('background.wav').play(loops=-1)

#Game Loop
while True:

    # DISPLAYSURF.fill(WHITE)
    #loops through map to set background
    for y in range(5):
        for x in range(10):
            location = (x*background.get_width(), y*background.get_height())
            DISPLAYSURF.blit(background, location)
    DISPLAYSURF.blit(font_small.render("Pontuação", True, RED), (10,10))
    pygame.draw.rect(DISPLAYSURF, GREEN, (int(DISPLAY[0]/3)-30, 0, 2, DISPLAY[1]), 50)

    for npc in enemies:

        npc.move(DISPLAY, npc_speed)

    P1.move(DISPLAY)
    P1.shoot(DISPLAY, all_shots)

    for shot in all_shots:
        shot.move(DISPLAY, shot_speed)
        shot.draw(DISPLAYSURF)

    for i in all_sprites:
        i.draw(DISPLAYSURF)

    for npc in enemies:
        if npc.getFinal(DISPLAY):
            gameOver(DISPLAYSURF, all_sprites, all_shots)


    #To be kill both sprites if collision occurs between shot and Enemy
    pygame.sprite.groupcollide(all_shots, enemies, True ,True)


    #Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Update all of the screen for software displays
    pygame.display.flip()
    # Setting the framerate to 30 fps
    clock.tick(30)
