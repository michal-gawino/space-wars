import os
import pygame
from root import PROJECT_IMAGES


class Image:

    def __init__(self, x, y, image_path):
        image_path = os.path.join(PROJECT_IMAGES, image_path)
        self.image = pygame.image.load(image_path).convert_alpha()
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

    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
