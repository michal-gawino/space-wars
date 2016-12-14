import os
from game_object import *
from root import PROJECT_IMAGES


class Missile(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'mine.png')

    def __init__(self, x, y, damage, speed):
        super().__init__(x, y)
        self.damage = damage
        self.speed = speed

    def move(self):
        self.rect.x += self.speed

class Rocket(Missile):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'missile.png')

    def __init__(self, x, y, damage, speed):
        super().__init__(x, y, damage, speed)

class GreenLaser(Missile):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'green_laser.png')

    def __init__(self, x, y, damage, speed):
        super().__init__(x, y, damage, -speed)

class Mine(Missile):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'mine.png')

    def __init__(self, x, y, damage, speed):
        super().__init__(x, y, damage, -speed)

class BlueLaser(Missile):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'blue_laser.png')

    def __init__(self, x, y, damage, speed):
        super().__init__(x, y, damage, speed)

class RedLaser(Missile):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'red_laser.png')

    def __init__(self, x, y, damage, speed):
        super().__init__(x, y, damage, speed)


class SpaceRing(Missile):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'ring.png')

    def __init__(self, x, y, damage, speed):
        super().__init__(x, y, damage, -speed)
