from game_objects import *

class Missile(GameObjects):

    def __init__(self, x, y, image, damage, speed):
        super().__init__(x, y, image)
        self.damage = damage
        self.speed = speed

    def move(self):
        self.rect.x -= self.speed
