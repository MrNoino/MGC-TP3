import pygame
from pygame.locals import *
import entity
from shot import Shot
from globals import *
import utils

class Player(entity.Entity):

    def __init__(self, username, type, position):

        self.__username = username

        self.__score = 0

        self.__speed_animation = 4
        self.__value = 0

        try:

            self._images = {"F": [[pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Run (1).png"), playerF_size),
                                pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Run (2).png"), playerF_size),
                                pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Run (3).png"), playerF_size),
                                pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Run (4).png"), playerF_size),
                                pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Run (5).png"), playerF_size),
                                pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Run (6).png"), playerF_size),
                                pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Run (7).png"), playerF_size),
                                pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Run (8).png"), playerF_size)]
                            ,   [pygame.transform.smoothscale(pygame.image.load("png/Adventure Girl/Shoot (1).png"), playerF_size)]]
                        	,"M": [[pygame.transform.smoothscale(pygame.image.load("png/RobotFree/Run (1).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/Run (2).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/Run (3).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/Run (4).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/Run (5).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/Run (6).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/Run (7).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/Run (8).png"), playerM_size)]
                        	,   [pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (1).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (2).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (3).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (4).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (5).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (6).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (7).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (8).png"), playerM_size),
                                pygame.transform.smoothscale(pygame.image.load("png/RobotFree/RunShoot (9).png"), playerM_size)]]}

        except Exception as e:

            #escreve um log com a exceção
            utils.saveLog(e)

            return

        self._images = self._images[type]

        super().__init__(self._images[0][0], position)

    def getUsername(self):

        return self.__username

    def shoot(self, windowSize, all_shots):

         # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if self.__value >= len(self._images[1])*self.__speed_animation:
            self.__value = 0
        print(len(self._images[1])*self.__speed_animation)
        print(int(self.__value/self.__speed_animation))

        if pygame.event.wait(10).type == KEYDOWN:
            if pygame.key.get_pressed()[K_SPACE]:

                super().setImage(self._images[1][int(self.__value/self.__speed_animation)])
                self.__value += 1


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
        
         # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if self.__value >= len(self._images[0])*self.__speed_animation:
            self.__value = 0
        print(len(self._images[0])*self.__speed_animation)
        print(int(self.__value/self.__speed_animation))
        __pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:

            if __pressed_keys[K_LEFT] or __pressed_keys[K_a]:

                super().move((-5, 0))
                super().setImage(self._images[0][int(self.__value/self.__speed_animation)])
                self.__value += 1

        if self.rect.right < int(windowSize[0] / 3):

            if __pressed_keys[K_RIGHT] or __pressed_keys[K_d]:

                super().move((5, 0))
                super().setImage(self._images[0][int(self.__value/self.__speed_animation)])
                self.__value += 1


        if self.rect.top > 0:

            if __pressed_keys[K_UP] or __pressed_keys[K_w]:

                super().move((0, -5))
                super().setImage(self._images[0][int(self.__value/self.__speed_animation)])
                self.__value += 1

        if self.rect.bottom < (windowSize[1]):

            if __pressed_keys[K_DOWN] or __pressed_keys[K_s]:

                super().move((0, 5))
                super().setImage(self._images[0][int(self.__value/self.__speed_animation)])
                self.__value += 1
