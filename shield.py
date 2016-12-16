import os
import pygame
from game_object import GameObject
from root import PROJECT_IMAGES


class Shield(GameObject):

    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'shield_small.png')

    def __init__(self, x, y):
        super().__init__(x, y)
        self.activated = False
        self.duration = 0

    def move(self):
        self.rect.y += 3

    def activate(self):
        if self.activated is False:
            self.image = pygame.image.load('images/shield.png').convert_alpha()
            self.activated = True

    def update(self, x, y):
        self.rect.x, self.rect.y = x, y
        self.duration += 1

    def deactivate(self):
        return self.duration == 300
