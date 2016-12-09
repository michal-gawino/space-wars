import pygame
from game_objects import GameObjects
from missile import Missile


class Player(GameObjects):

    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self.speed = 3
        self.health = 100
        self.missiles = 3
        self.blue_laser = 12
        self.timer = 25
        self.score = 0

    def motion(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.y - 3 > 30:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.y + 3 < 600 - self.image.get_height():
            self.rect.y += self.speed
        elif keys[pygame.K_LEFT] and self.rect.x + 3 > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.timer == 25:
            if keys[pygame.K_SPACE]:
                Missile(self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height()/2 - 8, 'red_laser.png', 0, 1)
                self.timer = 0
            elif keys[pygame.K_2] and self.missiles > 0:
                Missile(self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height()/2 - 8, 'missile.png', 2, 1)
                self.missiles -= 1
                self.timer = 0
            elif keys[pygame.K_1] and self.blue_laser > 0:
                Missile(self.rect.x + 80, self.rect.y + 10, 'blue_laser.png', 1, 1)
                Missile(self.rect.x + 80, self.rect.y + 55, 'blue_laser.png', 1, 1)
                self.blue_laser -= 1
                self.timer = 0

    def time_shooting(self):
        if self.timer < 25:
            self.timer += 1
