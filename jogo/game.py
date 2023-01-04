import pygame, sys
from pygame.locals import *
import random, time

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

background = pygame.image.load("Grass_Sample.png")


#Create a white screen
DISPLAYSURF = pygame.display.set_mode(DISPLAY)
#DISPLAYSURF.fill(WHITE)

pygame.display.set_caption("Zgame")

InitGraphics(DISPLAYSURF)
#pygame.mixer.Sound('background.wav').play(loops=-1)

#Game Loop
while True:
    # DISPLAYSURF.fill(WHITE)
    #loops through map to set background
    for y in range(5):
        for x in range(5):
            location = (x*704, y*320)
            DISPLAYSURF.blit(background, location)
    DISPLAYSURF.blit(font_small.render("Pontuação", True, RED), (10,10))
    #Cycles through all events occuring
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
