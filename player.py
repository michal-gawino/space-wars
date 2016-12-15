import os
import pygame
from game_object import GameObject
from missile import RedLaser, Rocket, BlueLaser
from root import PROJECT_IMAGES


class Player(GameObject):
    _IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'player.png')

    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = 3
        self.health = 100
        self.rockets = 3
        self.blue_laser = 12
        self.timer = 25
        self.score = 0

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.y > 55:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.y < 600 - self.image.get_height():
            self.rect.y += self.speed
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def shoot(self):
        keys = pygame.key.get_pressed()
        missile = None
        if self.timer == 25:
            if keys[pygame.K_SPACE]:
                missile = RedLaser(self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height()/2 - 7, 35, 3)
                self.timer = 0
            elif keys[pygame.K_2]:
                missile = Rocket(self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height()/2 - 15, 35, 3)
                self.timer = 0
            elif keys[pygame.K_1]:
                missile = [BlueLaser(self.rect.x + self.image.get_width(), self.rect.y + 5,  35, 3),
                           BlueLaser(self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height() - 24,  35, 3)]
                self.timer = 0
        return missile

    def time_shooting(self):
        if self.timer < 25:
            self.timer += 1
