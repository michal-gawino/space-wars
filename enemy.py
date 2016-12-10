import random
import math
from missile import *
from root import PROJECT_IMAGES


class Enemy(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'alien.png')

    def __init__(self, x, y, health, missile, speed):
        super().__init__(x, y)
        self.start_pos = y
        self.speed = speed
        self.amplitude = random.randint(1, 15)
        self.health = health
        self.missile = missile

    def move(self):
        self.rect.x -= self.speed
        self.rect.y = self.amplitude * math.sin(self.rect.x * 0.019) + self.start_pos
