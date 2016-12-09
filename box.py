from game_objects import *
from root import PROJECT_IMAGES
import os


class Box(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'box.png')

    def __init__(self, x, y):
        super().__init__(x, y)
        GameObject.objects.add(self)
        self.speed = 3

    def move(self):
        self.rect.y += self.speed
