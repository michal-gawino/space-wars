import random
from enemy import SpaceStation, Razor, Alien


class ShipFactory:

    @staticmethod
    def create():
        type_ = random.randint(0, 2)
        y = random.randrange(100, 500)
        if type_ == 0:
            return SpaceStation(810, y, 100, 1, 2)
        elif type_ == 1:
            return Razor(810, y, 125, 1, 2)
        else:
            return Alien(810, y, 155, 1, 2)
