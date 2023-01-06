import pygame
from pygame.locals import *
import random, time
import entity
import utils
from globals import *

class Shot(entity.Entity):
    # Atributes
    # rect
    
    
    def __init__(self, position):

        self.__speed_animation = 8
        self.__value = 0
        self.__value_dead = 0

        try:

            self.__img = [pygame.transform.smoothscale(pygame.image.load("png/Objects/Bullet_000.png"), shot_size),
                        pygame.transform.smoothscale(pygame.image.load("png/Objects/Bullet_001.png"), shot_size),
                        pygame.transform.smoothscale(pygame.image.load("png/Objects/Bullet_002.png"), shot_size),
                        pygame.transform.smoothscale(pygame.image.load("png/Objects/Bullet_003.png"), shot_size),
                        pygame.transform.smoothscale(pygame.image.load("png/Objects/Bullet_004.png"), shot_size)]
            self.__img_dead = [pygame.transform.smoothscale(pygame.image.load("png/Objects/Muzzle_000.png"), shot_dead),
                        pygame.transform.smoothscale(pygame.image.load("png/Objects/Muzzle_001.png"), shot_dead),
                        pygame.transform.smoothscale(pygame.image.load("png/Objects/Muzzle_002.png"), shot_dead)]

        except Exception as e:

            #escreve um log com a exceção
            utils.saveLog(e)

            return

        super().__init__(self.__img[0], position)
        rect = super().getRect()

    def setPosition(self, position):
        super().setPosition(position, 0)

    def move(self, displaySize, velocity):
        # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if self.__value >= len(self.__img)*self.__speed_animation:
            self.__value = 0

        super().move((velocity, 0))
        super().setImage(self.__img[int(self.__value/self.__speed_animation)])

        self.__value += 1

    def animatedead(self):
        if len(self.__img_dead)*self.__speed_animation > self.__value_dead:

            super().setImage(self.__img_dead[int(self.__value_dead/self.__speed_animation)])

            self.__value_dead += 1

        else:
            
            self.kill()