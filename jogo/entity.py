import pygame

class Entity(pygame.sprite.Sprite):

    _image = None

    def __init__(self, image, position):

        super().__init__()

        self._image = image

        self.rect = self._image.get_rect()

        self.rect.center = position

    def getImage(self):

        return self._image

    def setImage(self, image):

        self._image = image

    def getRect(self):

        return self.rect

    def _updateRect(self):

        self.rect = self._image.get_rect()

    def move(self, position):

        self.rect.move_ip(position[0], position[1])

    def draw(self, surface):

        surface.blit(self._image, self.rect)

    def reset(self, side, position):

        if side == 'Top':

            self.rect.top = 0

        elif side == 'Bottom':

            self.rect.bottom = 0

        elif side == 'Left':

            self.rect.left = 0

        elif side == 'Right':

            self.rect.right = 0

        elif side == 'Z':
            self.rect.midleft = position
        else:

            return False

        self.rect.center = position

        return True
