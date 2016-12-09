import os
from game_objects import *
from root import PROJECT_IMAGES


class Missile(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'mine.png')

    def __init__(self, x, y, damage, speed):
        super().__init__(x, y)
        self.damage = damage
        self.speed = speed

    def move(self):
        self.rect.x -= self.speed
