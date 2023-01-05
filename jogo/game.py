import pygame, sys
from pygame.locals import *
import random, time
from player import Player
from entity import Entity
from npc import Enemy

SPEED = 1

player_img = pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Idle (1).png"), (110,100))

DISPLAY = (800,500) #pygame.display.get_desktop_sizes
MID_DISPLAY = (int(DISPLAY[0]/2), int(DISPLAY[1]/2))
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)

def InitGraphics(DS):
    #pygame.mixer.Sound('background.wav').play(loops=-1)
    DS.fill(WHITE)
    global font_small
    DS.blit(font_small.render("Bem-Vindo ao Zgame!",True,BLUE), (50,50))
    pygame.display.flip()
    time.sleep(1)

#Initialzing
pygame.init()
# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background =  pygame.transform.smoothscale(pygame.image.load("Grass_Sample.jpg"),(200,200))


#Create a white screen
DISPLAYSURF = pygame.display.set_mode(DISPLAY)
#DISPLAYSURF.fill(WHITE)

pygame.display.set_caption("Zgame")
P1 = Player("P1", player_img, MID_DISPLAY)
E1 = Enemy((DISPLAY[0], random.randint(5,DISPLAY[1]-5)))
InitGraphics(DISPLAYSURF)
#pygame.mixer.Sound('background.wav').play(loops=-1)

#Game Loop
while True:
    # Setting the framerate to 30 fps
    clock.tick(30)
    # DISPLAYSURF.fill(WHITE)
    #loops through map to set background
    for y in range(5):
        for x in range(5):
            location = (x*background.get_width(), y*background.get_height())
            DISPLAYSURF.blit(background, location)
    DISPLAYSURF.blit(font_small.render("Pontuação", True, RED), (10,10))

    E1.move(SPEED, DISPLAY)
    P1.move(DISPLAY)
    E1.draw(DISPLAYSURF)
    P1.draw(DISPLAYSURF)


    #Cycles through all events occuring
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
