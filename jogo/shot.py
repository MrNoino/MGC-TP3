import pygame
from pygame.locals import *
import random, time
import entity

class Shot(entity.Entity):
    # Atributes
    # rect
    __speed_animation = 8
    __value = 0
    __img = [pygame.transform.smoothscale(pygame.image.load("png/Objects/Bullet_000.png"), (10,8))]

    def __init__(self, position):

        super().__init__(self.__img[0], position)
        rect = super().getRect()

    def move(self, displaySize, velocity):
        # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if self.__value >= len(self.__img)*self.__speed_animation:
            self.__value = 0
        super().move((velocity, 0))
        super().setImage(self.__img[int(self.__value/self.__speed_animation)])

        self.__value += 1

    def getPosition(self):
        return self.rect.left
