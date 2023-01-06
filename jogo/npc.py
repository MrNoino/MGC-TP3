import pygame
from pygame.locals import *
import random
import entity
import utils
from globals import *


class Enemy(entity.Entity):
    # Atributos do zumby
    
    def __init__(self, position):

        self.__speed_animation = 2
        self.__value = 0
        self.__value_dead = 0

        try:

            self._images = {"zumbiF": [[pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (1).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (2).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (3).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (4).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (5).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (6).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (7).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (8).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (9).png"), npcF_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (10).png"),npcF_size),True,False)]
                    ,[pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (1).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (2).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (3).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (4).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (5).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (6).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (7).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (8).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (9).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (10).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (11).png"),npcF_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Dead (12).png"),npcF_dead),True,False)]]
                    ,"zumbiM": [[pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (1).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (2).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (3).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (4).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (5).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (6).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (7).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (8).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (9).png"), npcM_size),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (10).png"),npcM_size),True,False)]
                    ,[pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (1).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (2).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (3).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (4).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (5).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (6).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (7).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (8).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (9).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (10).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (11).png"),npcM_dead),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Dead (12).png"),npcM_dead),True,False)]]}

        except Exception as e:

            #escreve um log com a exceção
            utils.saveLog(e)

            return

        rnd = random.randint(0, 1)

        self._images = self._images['zumbiF'] if rnd else self._images['zumbiM']

        super().__init__((self._images[0][0]), position)
            
    def setPosition(self, position):
        super().setPosition(position, 50)

    def getFinal(self, displaySize):

        if self.rect.left <= int(displaySize[0]/3):
            return True


    def move(self, displaySize, velocity):
        # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if self.__value >= len(self._images[0])*self.__speed_animation:
            self.__value = 0

        super().move((-velocity, 0))
        super().setImage(self._images[0][int(self.__value/self.__speed_animation)])

        self.__value += 1
        
        # top
        # super().move((0, -5))
        # bootom
        # super().move((0, 5))

    def animatedead(self):
        # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if len(self._images[1])*self.__speed_animation > self.__value_dead:

            super().setImage(self._images[1][int(self.__value_dead/self.__speed_animation)])

            self.__value_dead += 1

        else:
            
            self.kill()
        

        

