import random
import pygame
from box import Box
from missile import Missile
from player import Player
from enemy import Enemy


class Game:
    def __init__(self, game_screen, display_width=800, display_height=600):
        self.display_width = display_width
        self.display_height = display_height
        self.game_screen = game_screen
        self.frames_count = 0
        self.box = None
        self.player = Player(0, self.display_height/2)
        self.missiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

    def update_enemies(self):
        if self.frames_count % 180 == 0:
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
        self.missiles.draw(self.game_screen)
        self.enemies.draw(self.game_screen)
        self.game_screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        if self.box is not None:
            self.game_screen.blit(self.box.image, (self.box.rect.x, self.box.rect.y))
