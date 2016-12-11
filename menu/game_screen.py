import pygame
from game import Game
from image import Image
from menu.screen import Screen


class GameScreen(Screen):
    _HEALTH_IMAGE_PATH = 'health.jpg'
    _BAR_IMAGE_PATH = 'bar.png'

    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.game = Game(main_screen)
        self.top_bar = [Image(0, 0, self._BAR_IMAGE_PATH), Image(20, 4, self._HEALTH_IMAGE_PATH)]

    def draw(self):
        for image in self.top_bar:
            image.show(self.main_screen)

    def show(self):
        end = False
        clock = pygame.time.Clock()
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
            self.game.frames_count += 1
            self.game.update()
            self.main_screen.fill((0, 0, 0))
            self.game.draw()
            self.draw()
            clock.tick(60)
            pygame.display.update()
