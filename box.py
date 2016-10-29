from game_objects import *
import random


class Box(GameObjects):

    boxes = pygame.sprite.Group()

    def __init__(self, x, y, image):
        GameObjects.__init__(self, x, y, image)
        GameObjects.objects.add(self)
        Box.boxes.add(self)
        self.speed = 3

    def motion(self):
        self.rect.y += self.speed

    @staticmethod
    def movement():
        for box in Box.boxes:
            box.motion()

    @staticmethod
    def spawn(frames):
        if frames % 720 == 0:
            x = random.randint(30, 300)
            Box(x, -50, 'chest.png')