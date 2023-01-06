import pygame
from pygame.locals import *
import entity
from shot import Shot
from globals import *

class Player(entity.Entity):

    def __init__(self, username, image, position):

        self.__username = username

        self.__score = 0

        super().__init__(image, position)

    def getUsername(self):

        return self.__username

    def shoot(self, windowSize, all_shots):

        if pygame.event.wait(10).type == KEYDOWN:
            if pygame.key.get_pressed()[K_SPACE]:
                if len(all_shots.sprites()) < 10:

                    all_shots.add(Shot((self.rect.midright[0] -10, self.rect.midright[1])))

        for shot in all_shots:

            if shot.getPosition() > windowSize[0]:

                all_shots.remove(shot)

    def getScore(self):

        return self.__score

    def incrementScore(self, quantity):

        self.__score += quantity

    def move(self, windowSize):

        __pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:

            if __pressed_keys[K_LEFT] or __pressed_keys[K_a]:

                super().move((-10, 0))

        if self.rect.right < int(windowSize[0] / 3):

            if __pressed_keys[K_RIGHT] or __pressed_keys[K_d]:

                super().move((10, 0))


        if self.rect.top > 0:

            if __pressed_keys[K_UP] or __pressed_keys[K_w]:

                super().move((0, -10))

        if self.rect.bottom < (windowSize[1]):

            if __pressed_keys[K_DOWN] or __pressed_keys[K_s]:

                super().move((0, 10))
