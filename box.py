from game_object import *
from root import PROJECT_IMAGES
import os


class Box(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'chest.png')

    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 3

    def move(self):
        self.rect.y += self.speed
