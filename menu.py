import pygame

class Menu:
    def __init__(self):
        self.buttons = {'title.png': (100, 100), 'start.png': (200, 280), 'instruction.png': (200, 360),
                        'exit.png': (330, 440)}
        self.instructions = {'movement.png': (10, 50), 'shooting.png': (10, 370), 'mov1.png': (0, 120), 'mov2.png': (0, 220),
                             'sh1.png': (50, 425), 'sh2.png': (50, 480), 'back.png': (550, 500)}
        self.weapons = [('red_laser.png', (290, 440)), ('blue_laser.png', (145, 485)), ('blue_laser.png', (145, 505)),
                        ('missile.png', (140, 535))]

    def create_menu(self, screen):
        screen.blit(pygame.image.load('images/menu/menu.png').convert_alpha(), (0, 0))
        for filename, pos in self.buttons.items():
            screen.blit(pygame.image.load('images/menu/' + filename).convert_alpha(), pos)

    def highlight(self, screen, pos, width):
        line = pygame.image.load('images/blue_laser.png').convert_alpha()
        line = pygame.transform.scale(line, (width, 3))
        screen.blit(line, pos)

    def show_instruction(self, screen):
        screen.blit(pygame.image.load('images/menu/instruction_bg.png').convert_alpha(), (0, 0))
        for filename, pos in self.instructions.items():
            screen.blit(pygame.image.load('images/menu/' + filename).convert_alpha(), pos)
        for index, element in enumerate(self.weapons):
            img = pygame.image.load('images/' + element[0]).convert_alpha()
            screen.blit(img, element[1])