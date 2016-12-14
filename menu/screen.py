import pygame


class Screen:

    def __init__(self, main_screen):
        self.main_screen = main_screen

    def draw(self):
        raise NotImplementedError()

    def show(self):
        raise NotImplementedError()

    @staticmethod
    def is_mouse_on_button(button):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return button.x <= mouse_x <= button.x + button.width and \
               button.y <= mouse_y <= button.y + button.height

