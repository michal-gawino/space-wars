import itertools
import pygame
from image import Image
from menu.button import Button
from menu.screen import Screen


class InstructionScreen(Screen):
    _RED_LASER_PATH = 'red_laser.png'
    _BLUE_LASER_PATH = 'blue_laser.png'
    _MISSILE_PATH = 'missile.png'
    _MOVEMENT_LABEL_IMAGE_PATH = 'menu/movement.png'
    _SHOOTING_LABEL_IMAGE_PATH = 'menu/shooting.png'
    _MOVEMENT1_IMAGE_PATH = 'menu/mov1.png'
    _MOVEMENT2_IMAGE_PATH = 'menu/mov2.png'
    _SHOOTING1_IMAGE_PATH = 'menu/sh1.png'
    _SHOOTING2_IMAGE_PATH = 'menu/sh2.png'
    _BACK_BUTTON_IMAGE = 'menu/back.png'
    _BACKGROUND_IMAGE_PATH = 'menu/instruction_bg.png'

    def __init__(self, main_screen):
        super().__init__(main_screen)
        self.instructions = [Image(0, 0, self._BACKGROUND_IMAGE_PATH), Image(10, 50, self._MOVEMENT_LABEL_IMAGE_PATH),
                             Image(10, 370, self._SHOOTING_LABEL_IMAGE_PATH), Image(0, 120, self._MOVEMENT1_IMAGE_PATH),
                             Image(0, 200, self._MOVEMENT2_IMAGE_PATH), Image(50, 425, self._SHOOTING1_IMAGE_PATH),
                             Image(50, 470, self._SHOOTING2_IMAGE_PATH)]
        self.weapons = [Image(290, 440, self._RED_LASER_PATH), Image(145, 480, self._BLUE_LASER_PATH),
                        Image(145, 500, self._BLUE_LASER_PATH), Image(140, 525, self._MISSILE_PATH)]
        self.back_button = Button(550, 500, self._BACK_BUTTON_IMAGE)

    def draw(self):
        for image in itertools.chain(self.instructions, self.weapons):
            image.show(self.main_screen)
        self.back_button.show(self.main_screen)

    def show(self):
        instruction = True
        while instruction:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    instruction = False
            self.draw()
            if self.is_mouse_on_button(self.back_button):
                self.back_button.highlight(self.main_screen)
                if event.type == pygame.MOUSEBUTTONUP:
                    instruction = False
            pygame.display.update()
