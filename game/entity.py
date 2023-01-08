import pygame

class Entity(pygame.sprite.Sprite):

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

    def getPosition(self):
        return self.rect.center

    def setPosition(self, position, update):
        self.rect.center = (position[0]+update[0],position[1]+update[1])

    def move(self, position):

        self.rect.move_ip(position[0], position[1])

    def draw(self, surface):

        surface.blit(self._image, self.rect)

