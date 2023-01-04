import pygame

class Entity(pygame.sprite.Sprite):

    _image = None

    _rect = None

    def __init__(self, imagePath, position):

        super().__init__()

        self._image = pygame.image.load(imagePath)

        self._rect = self._image.get_rect()

        self._rect.center = position

    def getImage(self):

        return self._image

    def setImage(self, imagePath):

        self._image = pygame.image.load(imagePath)

        self._setRect()

    def getRect(self):

        return self._rect

    def _updateRect(self):

        self._rect = self.image.get_rect()

    def move(self, position):

        self.rect.move_ip(position[0], position[1])

    def draw(self, surface):

        surface.blit(self._image, self._rect)

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
        

