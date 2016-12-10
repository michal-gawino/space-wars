import os
import pygame
from root import PROJECT_IMAGES


class Button(pygame.sprite.Sprite):
    _LINE_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'blue_laser.png')

    def __init__(self, x, y, image):
        self.image = pygame.image.load(image).convert_alpha()
        line = pygame.image.load(self._LINE_IMAGE_PATH).convert_alpha()
        self.line = pygame.transform.scale(line, (self.image.get_width(), 3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    @property
    def width(self):
        return self.image.get_width()

    @property
    def height(self):
        return self.image.get_height()

    @property
    def x(self):
        return self.rect.x

    @property
    def y(self):
        return self.rect.y

    def highlight(self, screen):
        screen.blit(self.line, (self.rect.x, self.rect.y + self.image.get_height() + 10))

    def is_mouse_on(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.width and \
               self.y <= mouse_y <= self.y + self.height