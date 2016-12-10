import os
import pygame
from root import PROJECT_IMAGES


class Button(pygame.sprite.Sprite):
    _LINE_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'blue_laser.png')

    def __init__(self, x, y, image):
        line = pygame.image.load(self._LINE_IMAGE_PATH).convert_alpha()
        self.line = pygame.transform.scale(line, (self.image.width, 3))
        self.image = pygame.image.load(image).convert_alpha()
        self.image.rect.x = x
        self.image.rect.y = y

    @property
    def width(self):
        return self.image.width

    @property
    def height(self):
        return self.image.height

    @property
    def x(self):
        return self.image.rect.x

    @property
    def y(self):
        return self.image.rect.y

    def highlight(self, screen):
        screen.blit(self.line, (self.image.rect.x, self.image.rect.y + self.image.height + 10))

    def is_mouse_on(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and \
               self.y <= mouse_y <= self.y + self.height