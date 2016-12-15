import os
import pygame
from game_object import GameObject
from root import PROJECT_IMAGES


class Shield(GameObject):

    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'shield_small.png')

    def __init__(self, x, y):
        super().__init__(x, y)
        self.duration = 0
        self.activated = False

    def move(self):
        self.rect.y += 3

    def activate(self):
        if self.activated is False:
            self.image = pygame.image.load('images/shield.png').convert_alpha()
            self.activated = True

    def deactivate(self):
        self.duration += 1
        if self.duration == 420:
            return True

    def update(self, x, y):
        self.rect.x, self.rect.y = x, y
