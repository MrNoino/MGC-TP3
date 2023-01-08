import pygame
from pygame.locals import *
import random
import entity
import utils
from globals import *


class Enemy(entity.Entity):
    # Atributos do zumby
    
    def __init__(self, position):

        self.__speed_animation = 4
        self.__value = 0
        self.__value_dead = 0

        try:

            self._images = {"zumbiF": [[pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (1).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (2).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (3).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (4).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (5).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (6).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (7).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (8).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (9).png"), NPC_F_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Walk (10).png"),NPC_F_SIZE),True,False)]
                    ,[pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (1).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (2).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (3).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (4).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (5).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (6).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (7).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (8).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (9).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (10).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (11).png"),NPC_F_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/female/Dead (12).png"),NPC_F_DEAD),True,False)]]
                    ,"zumbiM": [[pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (1).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (2).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (3).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (4).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (5).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (6).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (7).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (8).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (9).png"), NPC_M_SIZE),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Walk (10).png"),NPC_M_SIZE),True,False)]
                    ,[pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (1).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (2).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (3).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (4).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (5).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (6).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (7).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (8).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (9).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (10).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (11).png"),NPC_M_DEAD),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("images/male/Dead (12).png"),NPC_M_DEAD),True,False)]]}

        except Exception as e:

            #escreve um log com a exceção
            utils.saveLog(e)

            return

        rnd = random.randint(0, 1)

        self._images = self._images['zumbiF'] if rnd else self._images['zumbiM']

        super().__init__((self._images[0][0]), position)
            
    def setPosition(self, position):
        super().setPosition(position, (-50,0))

    def getFinal(self):

        if self.rect.left <= 0:
            return True


    def move(self, velocity):
        # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if self.__value >= len(self._images[0])*self.__speed_animation:
            self.__value = 0

        super().move((-velocity, 0))
        super().setImage(self._images[0][int(self.__value/self.__speed_animation)])

        self.__value += 1

    def animateDead(self):
        # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if len(self._images[1])*self.__speed_animation > self.__value_dead:

            super().setImage(self._images[1][int(self.__value_dead/self.__speed_animation)])

            self.__value_dead += 1

        else:
            
            self.kill()
        
        return False
        
        

