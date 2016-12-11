import os
import pygame
from root import PROJECT_IMAGES

class FinalScreen:
    _BACKGROUND_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'final_screen.png')

    def __init__(self):
        self.background = pygame.image.load(self._BACKGROUND_IMAGE_PATH).convert_alpha()

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

    def handle_event(self):
        final_screen = True
        while final_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    final_screen = False
            pygame.display.update()

