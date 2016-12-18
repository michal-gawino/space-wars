import os
import pygame
from menu.button import Button
from menu.screen import Screen
from root import PROJECT_IMAGES

class GameWonScreen(Screen):
    _BACKGROUND_IMAGE_PATH = os.path.join(PROJECT_IMAGES, 'menu/game_won_background.png')
    _BACK_BUTTON_IMAGE = 'menu/back.png'

    def __init__(self, main_screen):
        super().__init__(main_screen)
        self.background = pygame.image.load(self._BACKGROUND_IMAGE_PATH).convert_alpha()
        self.font = pygame.font.SysFont("arial", 28)
        self.button = Button(600, 500, self._BACK_BUTTON_IMAGE)

    def draw(self, score):
        label = self.font.render('Congratulations, you\'ve completed the game.' + 'Final score: {}'.format(score),
                                 1, (255, 255, 255))
        self.main_screen.blit(self.background, (0, 0))
        self.main_screen.blit(label, (40, 300))

    def show(self, score):
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.draw(score)
            self.button.show(self.main_screen)
            if self.is_mouse_on_button(self.button):
                self.button.highlight(self.main_screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    end = True
            pygame.display.update()
