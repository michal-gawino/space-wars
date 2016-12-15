import pygame
from game import Game
from menu.screen import Screen


class GameScreen(Screen):

    def __init__(self, main_screen):
        super().__init__(main_screen)
        self.game = Game(main_screen)

    def draw(self):
        pass

    def show(self):
        end = False
        clock = pygame.time.Clock()
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
            self.game.frames_count += 1
            self.game.update()
            self.main_screen.fill((0, 0, 0))
            self.game.draw()
            self.draw()
            clock.tick(60)
            pygame.display.update()
