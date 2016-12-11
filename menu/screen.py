import pygame


class Screen:

    def draw(self):
        pass

    def show(self):
        pass

    @staticmethod
    def is_mouse_on_button(button):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return button.x <= mouse_x <= button.x + button.width and \
               button.y <= mouse_y <= button.y + button.height

