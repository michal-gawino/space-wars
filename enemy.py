from missile import *
from root import PROJECT_IMAGES
from strategy import MovementStrategy


class Enemy(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'alien.png')

    def __init__(self, x, y, health, missile, speed):
        super().__init__(x, y)
        self.start_y = y
        self.speed = speed
        self.health = health
        self.missile = missile

    def move(self):
        self.rect.x, self.rect.y = MovementStrategy.execute(self.rect.x, self.rect.y, self.start_y)

class Alien(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'alien.png')

    def __init__(self, x, y, health, missile, speed):
        super().__init__(x, y, health, missile, speed)


class Razor(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'razor.png')

    def __init__(self, x, y, health, missile, speed):
        super().__init__(x, y, health, missile, speed)


class SpaceStation(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'space_station.png')

    def __init__(self, x, y, health, missile, speed):
        super().__init__(x, y, health, missile, speed)

