import random
import pygame
from box import Box
from missile import SpaceRing
from player import Player
from enemy import Enemy, Alien, Razor, SpaceStation


class Game:
    def __init__(self, main_screen):
        self.display_width, self.display_height = main_screen.get_size()
        self.main_screen = main_screen
        self.frames_count = 0
        self.box = None
        self.player = Player(0, self.display_height/2)
        self.missiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

    def update_enemies(self):
        if self.frames_count % 180 == 0:
            enemy = SpaceStation(800, 300, 100, 1, 3)
            self.enemies.add(enemy)
            self.missiles.add(SpaceRing(enemy.rect.x, enemy.rect.y, 1, 5))
        for enemy in self.enemies:
            enemy.move()
            if enemy.health < 0:
                self.enemies.remove(enemy)

    def update_missiles(self):
        for missile in self.missiles:
            missile.move()

    def update_box(self):
        if self.frames_count % 720 == 0:
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
        self.missiles.draw(self.main_screen)
        self.enemies.draw(self.main_screen)
        self.main_screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        if self.box is not None:
            self.main_screen.blit(self.box.image, (self.box.rect.x, self.box.rect.y))
