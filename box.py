from game_objects import *


class Box(GameObjects):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        GameObjects.objects.add(self)
        self.speed = 3

    def move(self):
        self.rect.y += self.speed
