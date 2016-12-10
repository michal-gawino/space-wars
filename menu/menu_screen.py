import os
import pygame
from menu.button import Button
from root import MENU_IMAGES


class MenuScreen:
    _BACKGROUND_PATH = os.path.join(MENU_IMAGES, 'menu.png')
    _TITLE_IMAGE_PATH = os.path.join(MENU_IMAGES, 'title.png')
    _START_GAME_BUTTON_PATH = os.path.join(MENU_IMAGES, 'start.png')
    _INSTRUCTION_BUTTON_PATH = os.path.join(MENU_IMAGES, 'instruction.png')
    _EXIT_BUTTON_PATH = os.path.join(MENU_IMAGES, 'exit.png')

    def __init__(self):
        self.buttons = [Button(200, 280, self._START_GAME_BUTTON_PATH), Button(200, 360, self._INSTRUCTION_BUTTON_PATH),
                        Button(330, 440, self._EXIT_BUTTON_PATH)]
        self.background = pygame.image.load(self._BACKGROUND_PATH).convert_alpha()
        self.title = pygame.image.load(self._TITLE_IMAGE_PATH)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.title, (100, 100))
        for button in self.buttons:
            screen.blit(button.image, (button.rect.x, button.rect.y))

    def highlight(self, screen, mouse_x, mouse_y):
        for button in self.buttons:
            if button.is_mouse_on(mouse_x, mouse_y):
                button.highlight(screen)
                break
