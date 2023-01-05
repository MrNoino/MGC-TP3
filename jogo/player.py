import pygame
from pygame.locals import *
import entity
from shot import Shot
from globals import *

class Player(entity.Entity):

    __username = None

    def __init__(self, username, image, position):

        self.__username = username

        super().__init__(image, position)

    def getUsername(self):

        return self.__username

    def shoot(self, windowSize, all_shots):

        if pygame.event.wait(10).type == KEYDOWN:
            if pygame.key.get_pressed()[K_SPACE]:
                if len(all_shots.sprites()) < 10:

                    all_shots.add(Shot(self.rect.midright))

        for shot in all_shots:
            if shot.getPosition() > windowSize[0]:
                all_shots.remove(shot)


    def move(self, windowSize):

        __pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:

            if __pressed_keys[K_LEFT] or __pressed_keys[K_a]:

                super().move((-5, 0))

        if self.rect.right < int(windowSize[0] / 3):

            if __pressed_keys[K_RIGHT] or __pressed_keys[K_d]:

                super().move((5, 0))


        if self.rect.top > 0:

            if __pressed_keys[K_UP] or __pressed_keys[K_w]:

                super().move((0, -5))

        if self.rect.bottom < (windowSize[1] - 25):

            if __pressed_keys[K_DOWN] or __pressed_keys[K_s]:

                super().move((0, 5))
