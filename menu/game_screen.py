import pygame
from game import Game
from image import Image
from menu.game_over_screen import GameOverScreen
from menu.game_won_screen import GameWonScreen
from menu.screen import Screen
from star import Star


class GameScreen(Screen):

    def __init__(self, main_screen):
        super().__init__(main_screen)
        self.game = Game(main_screen)
        self.stars = Star(30)
        self.game_over_screen = GameOverScreen(main_screen)
        self.game_won_screen = GameWonScreen(main_screen)
        self.background = Image(0, 0, 'background.png')

    def draw(self):
        pass

    def show(self):
        end = False
        self.game.reset()
        clock = pygame.time.Clock()
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.game.frames_count += 1
            self.game.update()
            self.background.show(self.main_screen)
            self.stars.draw(self.main_screen)
            self.game.draw()
            self.draw()
            if self.game.player.health <= 0:
                self.game_over_screen.show(self.game.player.score)
                end = True
            if self.game.level.current_level == 3 and self.game.level.levels[self.game.level.current_level] == 0:
                self.game_won_screen.show(self.game.player.score)
                end = True
            clock.tick(60)
            pygame.display.update()
