import pygame

class Entity(pygame.sprite.Sprite):

    _image = None

    _rect = None

    def __init__(self, image, position):

        super().__init__()

        self._image = image

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

        self._rect.move_ip(position[0], position[1])

    def draw(self, surface):

        surface.blit(self._image, self._rect)

    def reset(self, side, position):

        if side == 'Top':

            self._rect.top = 0

        elif side == 'Bottom':

            self._rect.bottom = 0

        elif side == 'Left':

            self._rect.left = 0

        elif side == 'Right':

            self._rect.right = 0

        else:

            return False

        self._rect.center = position

        return True
