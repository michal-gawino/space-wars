import os
import pygame
from root import PROJECT_IMAGES


class TopBar:
    _HEALTH_BAR_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'bar.png')
    _MISSLE_POS_X = 220

    def __init__(self):
        self.health_bar = pygame.image.load(self._HEALTH_BAR_IMAGE_PATH).convert_alpha()
        self.health = ImageLoader(self._HEALTH_BAR_IMAGE_PATH).load()

    def draw(self, screen):
        screen.blit(self.health_bar, (10, 10))
        screen.blit(self.health, (30, 14))
        missile = pygame.image.load('images/missile_small.png').convert_alpha()
        laser = pygame.image.load('images/blue_laser.png').convert_alpha()
        screen.blit(missile, (self._MISSLE_POS_X, 18))
        screen.blit(laser, (340, 18))
        screen.blit(laser, (340, 32))

class ImageLoader:

    def __init__(self, image_path):
        self.image_path = image_path

    def load(self):
        return pygame.image.load(self.image_path).convert_alpha()
