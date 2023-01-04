import pygame
from pygame.locals import *
import entity

class Player(entity.Entity):

    __username = None

    def __init__(self, username, imagePath, position):

        self.__username = username

        super.__init__(imagePath, position)

    def getUsername(self):

        return self.__username

    def shoot(self):

        1 == 1

    def move(self, windowSize):

        __pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:

            if __pressed_keys[K_LEFT] or __pressed_keys[K_a]:

                super().move((-5, 0))

        if self.rect.right < windowSize[0]: 

            if __pressed_keys[K_RIGHT] or __pressed_keys[K_d]:

                super().move((5, 0))

        if self.rect.Top > 0: 

            if __pressed_keys[K_UP] or __pressed_keys[K_w]:

                super().move(0, 5)

        if self.rect.bottom > windowSize[1]: 

            if __pressed_keys[K_DOWN] or __pressed_keys[K_s]:

                super().move(0, -5)
