import os
import pygame
from menu.button import Button
from root import PROJECT_IMAGES, MENU_IMAGES


class InstructionScreen:
    _RED_LASER_PATH = os.path.join(PROJECT_IMAGES, 'red_laser.png')
    _BLUE_LASER_PATH = os.path.join(PROJECT_IMAGES, 'blue_laser.png')
    _MISSILE_PATH = os.path.join(PROJECT_IMAGES, 'missile.png')
    _MOVEMENT_LABEL_IMAGE_PATH = os.path.join(MENU_IMAGES, 'movement.png')
    _SHOOTING_LABEL_IMAGE_PATH = os.path.join(MENU_IMAGES, 'shooting.png')
    _MOVEMENT1_IMAGE_PATH = os.path.join(MENU_IMAGES, 'mov1.png')
    _MOVEMENT2_IMAGE_PATH = os.path.join(MENU_IMAGES, 'mov2.png')
    _SHOOTING1_IMAGE_PATH = os.path.join(MENU_IMAGES, 'sh1.png')
    _SHOOTING2_IMAGE_PATH = os.path.join(MENU_IMAGES, 'sh2.png')
    _BACK_BUTTON_IMAGE = os.path.join(MENU_IMAGES, 'back.png')
    _BACKGROUND_IMAGE_PATH = os.path.join(MENU_IMAGES, 'instruction_bg.png')

    def __init__(self):
        self.instructions = {self._MOVEMENT_LABEL_IMAGE_PATH: (10, 50), self._SHOOTING_LABEL_IMAGE_PATH: (10, 370),
                             self._MOVEMENT1_IMAGE_PATH: (0, 120), self._MOVEMENT2_IMAGE_PATH: (0, 220),
                             self._SHOOTING1_IMAGE_PATH: (50, 425), self._SHOOTING2_IMAGE_PATH: (50, 480)}
        self.weapons = [(self._RED_LASER_PATH, (290, 440)), (self._BLUE_LASER_PATH, (145, 485)),
                        (self._BLUE_LASER_PATH, (145, 505)), (self._MISSILE_PATH, (140, 535))]
        self.back_button = Button(550, 500, self._BACK_BUTTON_IMAGE)
        self.background = pygame.image.load(self._BACKGROUND_IMAGE_PATH)

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        for image, position in self.instructions.items():
            screen.blit(pygame.image.load(image).convert_alpha(), position)
        for image, position in self.weapons:
            screen.blit(pygame.image.load(image).convert_alpha(), position)
