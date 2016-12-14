import os
import pygame
from menu.screen import Screen
from root import PROJECT_IMAGES

class FinalScreen(Screen):
    _BACKGROUND_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'final_screen.png')

    def __init__(self, main_screen):
        super().__init__(main_screen)
        self.background = pygame.image.load(self._BACKGROUND_IMAGE_PATH).convert_alpha()

    def draw(self, screen):
        self.main_screen.blit(self.background, (0, 0))

    def show(self):
        pass

