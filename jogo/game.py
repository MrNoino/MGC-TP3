import pygame, sys
from pygame.locals import *
import random, time
from player import Player
from entity import Entity

value = 0
image_zumbiF = [pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (1).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (2).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (3).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (4).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (5).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (6).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (7).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (8).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (9).png"), (90,100)),True,False),
                pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (10).png"),(90,100)),True,False)]


DISPLAY = (800,500) #pygame.display.get_desktop_sizes

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
    time.sleep(2)

#Initialzing
pygame.init()
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("Grass_Sample2.png")


#Create a white screen
DISPLAYSURF = pygame.display.set_mode(DISPLAY)
#DISPLAYSURF.fill(WHITE)

pygame.display.set_caption("Zgame")

P1 = Player("P1", image_zumbiF[0],(int(DISPLAY[0]/2), int(DISPLAY[1]/2)))

InitGraphics(DISPLAYSURF)
#pygame.mixer.Sound('background.wav').play(loops=-1)

#Game Loop
while True:


    # DISPLAYSURF.fill(WHITE)
    #loops through map to set background
    for y in range(5):
        for x in range(5):
            location = (x*658, y*369)
            DISPLAYSURF.blit(background, location)
    DISPLAYSURF.blit(font_small.render("Pontuação", True, RED), (10,10))
    P1.move(DISPLAY)


    P1.draw(DISPLAYSURF)


    #Cycles through all events occuring
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    value += 1
