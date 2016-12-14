import itertools
import pygame
from image import Image
from menu.button import Button
from menu.game_screen import GameScreen
from menu.instruction_screen import InstructionScreen
from menu.screen import Screen


class MenuScreen(Screen):

    def __init__(self, main_screen):
        super().__init__(main_screen)
        self.instruction_screen = InstructionScreen(main_screen)
        self.game_screen = GameScreen(main_screen)
        start_button = Button(200, 280, 'menu/start.png')
        instructions_button = Button(200, 360, 'menu/instruction.png')
        exit_button = Button(330, 440, 'menu/exit.png')
        self.button_actions = dict()
        self.button_actions[start_button] = self.game_screen.show
        self.button_actions[instructions_button] = self.instruction_screen.show
        self.button_actions[exit_button] = quit
        self.images = [Image(0, 0, 'menu/menu.png'), Image(100, 100, 'menu/title.png')]

    def draw(self):
        for image in itertools.chain(self.images, self.button_actions):
            image.show(self.main_screen)

    def show(self):
        exit_ = False
        while not exit_:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
                self.draw()
                for button, action in self.button_actions.items():
                    if self.is_mouse_on_button(button):
                        button.highlight(self.main_screen)
                        if event.type == pygame.MOUSEBUTTONUP:
                            action()
                pygame.display.update()
