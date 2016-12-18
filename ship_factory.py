import random
from enemy import SpaceStation, Razor, Alien


class ShipFactory:

    @staticmethod
    def create():
        type_ = random.randint(0, 2)
        y = random.randrange(100, 500)
        speed = random.randint(1, 2)
        if type_ == 0:
            if y > 300:
                speed *= -1
            return SpaceStation(810, y, 100, speed, 10)
        elif type_ == 1:
            return Razor(810, y, 125, speed, 20)
        else:
            return Alien(810, y, 150, speed, 30)