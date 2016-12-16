from missile import *
from root import PROJECT_IMAGES
from strategy import MovementStrategy


class Enemy(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'alien.png')

    def __init__(self, x, y, health, speed):
        super().__init__(x, y)
        self.start_y = y
        self.health = health
        self.speed = speed
        self.timer = 0

    def move(self):
        self.rect.x, self.rect.y = MovementStrategy.execute(self.rect.x, self.rect.y, self.speed, self.start_y)

    def attack(self):
        pass

    def time_shooting(self):
        if self.timer < 120:
            self.timer += 1


class Alien(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'alien.png')

    def __init__(self, x, y, health, speed):
        super().__init__(x, y, health, speed)

    def attack(self):
        if self.timer == 120:
            self.timer = 0
            return YellowBeam(self.rect.x - 100, self.rect.y + 20, 1, self.speed + 1)


class Razor(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'razor.png')

    def __init__(self, x, y, health, speed):
        super().__init__(x, y, health, speed)

    def attack(self):
        if self.timer == 120:
            self.timer = 0
            return Mine(self.rect.x - 30, self.rect.y + 30, 1, self.speed + 1)


class SpaceStation(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'space_station.png')

    def __init__(self, x, y, health, speed):
        super().__init__(x, y, health, speed)

    def attack(self):
        if self.timer == 60:
            self.timer = 0
            return SpaceRing(self.rect.x - 100, self.rect.y + 50, 1, self.speed + 1)

