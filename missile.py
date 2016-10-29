from game_objects import *

class Missile(GameObjects):

    missiles = pygame.sprite.Group()

    def __init__(self, x, y, image, missile_type):
        GameObjects.__init__(self, x, y, image)
        Missile.missiles.add(self)
        self.missile_type = missile_type
        self.types = {0: [30, 2], 1: [40, 3], 2: [95, 3], 3: [30, -2], 4: [17, -2], 5: [60, -2]}
        self.damage, self.speed = self.types[missile_type]

    def motion(self):
        self.rect.x += self.speed

    @staticmethod
    def movement():
        for missile in Missile.missiles:
            missile.motion()