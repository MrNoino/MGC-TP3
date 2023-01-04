import pygame

class Entity(pygame.sprite.Sprite):

    __image = None

    __rect = None

    def __init__(self, imagePath, position):

        super().__init__()

        self.__image = pygame.image.load(imagePath)

        self.__rect = self.__image.get__rect()

        self.__rect.center = position

    def getImage(self):

        return self.__image

    def setImage(self, imagePath):

        self.__image = pygame.image.load(imagePath)

        self._setRect()

    def getRect(self):

        return self.__rect

    def _updateRect(self):

        self.__rect = self.image.get__rect()

    def move(self, position):

        self.rect.move_ip(position[0], position[1])

        

    def reset(self, side, position):

        if side == 'Top':

            self.rect.top = 0

        elif side == 'Bottom':

            self.rect.bottom = 0

        elif side == 'Left':

            self.rect.left = 0

        elif side == 'Right':

            self.rect.right = 0

        else:

            return False

        
        self.rect.center = position

        return True
        

