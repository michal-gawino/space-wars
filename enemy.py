from missile import *
from root import PROJECT_IMAGES


class Enemy(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'alien.png')

    def __init__(self, x, y, health, speed, points, strategy):
        super().__init__(x, y)
        self.start_y = y
        self.health = health
        self.speed = speed
        self.points = points
        self.timer = 0
        self.strategy = strategy

    def move(self):
        self.check_boundary()
        self.rect.x, self.rect.y = self.strategy.execute(self.rect.x, self.rect.y, self.speed, self.start_y)

    def attack(self):
        pass

    def check_boundary(self):
        if self.rect.y < 50 or self.rect.y > 550:
            self.speed *= -1

    def time_shooting(self):
        if self.timer < 120:
            self.timer += 1


class Alien(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'alien.png')

    def __init__(self, x, y, health, speed, points):
        super().__init__(x, y, health, speed, points)

    def attack(self):
        if self.timer == 120:
            self.timer = 0
            return YellowBeam(self.rect.x - 60, self.rect.y + 20, 32, abs(self.speed) + 1)


class Razor(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'razor.png')

    def __init__(self, x, y, health, speed, points):
        super().__init__(x, y, health, speed, points)

    def attack(self):
        if self.timer == 120:
            self.timer = 0
            return Mine(self.rect.x - 30, self.rect.y + 20, 23, abs(self.speed) + 1)


class SpaceStation(Enemy):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'space_station.png')

    def __init__(self, x, y, health, speed, points):
        super().__init__(x, y, health, speed, points)

    def attack(self):
        if self.timer == 100:
            self.timer = 0
            return SpaceRing(self.rect.x - 40, self.rect.y + 20, 19, abs(self.speed) + 1)
