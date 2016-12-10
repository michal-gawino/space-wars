import os
import pygame
from root import PROJECT_IMAGES


class FinalScreen:
    _BACKGROUND_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'final_screen.png')

    def __init__(self):
        self.background = pygame.image.load(self._BACKGROUND_IMAGE_PATH).convert_alpha()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
