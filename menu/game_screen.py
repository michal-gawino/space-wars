import os
import pygame
from root import PROJECT_IMAGES

class GameScreen:
    _HEALTH_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'health.jpg')
    _BAR_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'bar.png')

    def __init__(self):
        self.top_bar = [(self._BAR_IMAGE_PATH, (0, 0)), (self._HEALTH_IMAGE_PATH, (20, 4))]

    def draw(self, screen):
        screen.fill((0, 0, 0))
        for image, position in self.top_bar:
            screen.blit(pygame.image.load(image).convert_alpha(), position)

    def handle_event(self, game):
        game.game_loop()
