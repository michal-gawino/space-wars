import pygame
from menu.menu_screen import MenuScreen

def run_game():
    pygame.init()
    pygame.display.set_caption('Space Wars')
    pygame.display.init()
    screen = pygame.display.set_mode((800, 600))
    menu = MenuScreen(screen)
    menu.show()

if __name__ == '__main__':
    run_game()
