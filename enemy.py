import random
import math
from missile import *


class Enemy(GameObjects):

    def __init__(self, x, y, image, health, missile, speed):
        super().__init__(x, y, image)
        self.start_pos = y
        self.speed = speed
        self.amplitude = random.randint(1, 15)
        self.health = health
        self.missile = missile

    def move(self):
        self.rect.x -= self.speed
        self.rect.y = self.amplitude * math.sin(self.rect.x * 0.019) + self.start_pos
