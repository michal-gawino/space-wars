import pygame
from menu.button import Button


class MenuScreen:
    def __init__(self):
        self.buttons = [Button(100, 100, 'title.png'), Button(200, 280, 'start.png'), Button(200, 360, 'instruction.png'),
                        Button(330, 440, 'exit.png')]
        self.instructions = {'movement.png': (10, 50), 'shooting.png': (10, 370), 'mov1.png': (0, 120), 'mov2.png': (0, 220),
                             'sh1.png': (50, 425), 'sh2.png': (50, 480), 'back.png': (550, 500)}
        self.weapons = [('red_laser.png', (290, 440)), ('blue_laser.png', (145, 485)), ('blue_laser.png', (145, 505)),
                        ('missile.png', (140, 535))]

    def create_menu(self, screen):
        screen.blit(pygame.image.load('images/menu/menu.png').convert_alpha(), (0, 0))
        for button in self.buttons:
            button.blit(screen)

    def highlight(self, screen, mouse_x, mouse_y):
        for button in self.buttons:
            if button.is_mouse_on(mouse_x, mouse_y):
                button.highlight(screen)
                break