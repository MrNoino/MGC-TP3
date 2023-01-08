import pygame
import entity
import utils
from globals import *

class Shot(entity.Entity):   
    
    def __init__(self, position):

        self.__speed_animation = 8
        self.__value = 0
        self.__value_dead = 0

        try:

            self.__img = [pygame.transform.smoothscale(pygame.image.load("images/Objects/Bullet_000.png"), SHOT_SIZE),
                        pygame.transform.smoothscale(pygame.image.load("images/Objects/Bullet_001.png"), SHOT_SIZE),
                        pygame.transform.smoothscale(pygame.image.load("images/Objects/Bullet_002.png"), SHOT_SIZE),
                        pygame.transform.smoothscale(pygame.image.load("images/Objects/Bullet_003.png"), SHOT_SIZE),
                        pygame.transform.smoothscale(pygame.image.load("images/Objects/Bullet_004.png"), SHOT_SIZE)]
            self.__img_dead = [pygame.transform.smoothscale(pygame.image.load("images/Objects/Muzzle_000.png"), SHOT_DEAD),
                        pygame.transform.smoothscale(pygame.image.load("images/Objects/Muzzle_001.png"), SHOT_DEAD),
                        pygame.transform.smoothscale(pygame.image.load("images/Objects/Muzzle_002.png"), SHOT_DEAD),
                        pygame.transform.smoothscale(pygame.image.load("images/Objects/Muzzle_003.png"), SHOT_DEAD),
                        pygame.transform.smoothscale(pygame.image.load("images/Objects/Muzzle_004.png"), SHOT_DEAD)]

        except Exception as e:

            #escreve um log com a exceção
            utils.saveLog(e)

            return

        super().__init__(self.__img[0], position)

    def setPosition(self, position):
        super().setPosition(position, (30,-10))

    def move(self, velocity):
        # Define qual imagem do array será usada, é necessário para que uma imagem dure mais tempo, assim a animação se completa num maior tempo.
        if self.__value >= len(self.__img)*self.__speed_animation:
            self.__value = 0
        else:
            super().setImage(self.__img[int(self.__value/self.__speed_animation)])
            self.__value += 1

        super().move((velocity, 0))

    def animateDead(self):
        
        if len(self.__img_dead)*self.__speed_animation > self.__value_dead:

            super().setImage(self.__img_dead[int(self.__value_dead/self.__speed_animation)])
            
            self.__value_dead += 1

        else:
            
            self.kill()
        
        return False