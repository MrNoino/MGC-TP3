import pygame
from pygame.locals import *
import random, time
import entity


class Enemy(entity.Entity):
    # Atributos do zumby
    __speed_animation = 8
    __value = 0
    __image_zumbiF = [pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (1).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (2).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (3).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (4).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (5).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (6).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (7).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (8).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (9).png"), (90,100)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/female/Walk (10).png"),(90,100)),True,False)]
    __image_zumbiM = [pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (1).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (2).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (3).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (4).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (5).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (6).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (7).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (8).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (9).png"), (80,90)),True,False),
                    pygame.transform.flip(pygame.transform.smoothscale(pygame.image.load("png/male/Walk (10).png"),(80,90)),True,False)]


    def __init__(self, position):

        super().__init__(self.__image_zumbiF[0], position)


    def getFinal(self, displaySize):

        if self.rect.left <= int(displaySize[0]/3):
            return True


    def move(self, displaySize, velocity):
        # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if self.__value >= len(self.__image_zumbiF)*self.__speed_animation:
            self.__value = 0

        super().move((-velocity, 0))
        super().setImage(self.__image_zumbiF[int(self.__value/self.__speed_animation)])

        self.__value += 1

        if self.rect.right < 0:

            self.reset("Z", (displaySize[0], random.randint(50,displaySize[1]-50)))
        #     Game-over
        #
        # top
        # super().move((0, -5))
        # bootom
        # super().move((0, 5))
