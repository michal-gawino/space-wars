import os
import random
import pygame
from box import Box
from menu.menu_screen import MenuScreen
from missile import Missile
from player import Player
from enemy import Enemy

os.environ['SDL_VIDEO_CENTERED'] = '1'


class Game:
    def __init__(self):
        self.display_width = 800
        self.display_height = 600
        self.frames = 0
        self.box = None
        self.player = None
        self.missiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.game_display = pygame.display.set_mode((self.display_width, self.display_height))

    def update_enemies(self):
        if self.frames % 180 == 0:
            enemy = Enemy(100, 100, 100, 1, 1)
            self.enemies.add(enemy)
            self.missiles.add(Missile(enemy.rect.x, enemy.rect.y, 1, 1))
        for enemy in self.enemies:
            enemy.move()
            if enemy.health < 0:
                self.enemies.remove(enemy)

    def update_missiles(self):
        for missile in self.missiles:
            missile.move()

    def update_box(self):
        if self.frames % 720 == 0:
            x = random.randint(30, 300)
            self.box = Box(x, -50)
        if self.box is not None:
            self.box.move()

    def update_player(self):
        self.player.move()

    def update(self):
        self.update_player()
        self.update_missiles()
        self.update_enemies()
        self.update_box()

    def draw(self):
        self.missiles.draw(self.game_display)
        self.enemies.draw(self.game_display)
        self.game_display.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        if self.box is not None:
            self.game_display.blit(self.box.image, (self.box.rect.x, self.box.rect.y))

    def run(self):
        pygame.display.set_caption('Space Wars')
        pygame.mouse.set_visible(True)
        pygame.init()
        menu = MenuScreen()
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                mouse_x, mouse_y = pygame.mouse.get_pos()
                menu.draw(self.game_display)
                menu.handle_event(self.game_display, event, mouse_x, mouse_y, self)
            pygame.display.update()

    def game_loop(self):
        clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        self.player = Player(0, self.display_height/2)
        end = False
        while not end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
            self.frames += 1
            self.update()
            self.game_display.fill((0, 0, 0))
            self.draw()
            pygame.display.update()
            clock.tick(60)
