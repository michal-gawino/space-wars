import random
import pygame
from animation import BlueExplosion, RedExplosion
from box import Box
from player import Player
from shield import Shield
from ship_factory import ShipFactory
from pygame.sprite import collide_rect, spritecollide


class Game:
    def __init__(self, main_screen):
        self.display_width, self.display_height = main_screen.get_size()
        self.main_screen = main_screen
        self.frames_count = 0
        self.box = None
        self.shield = None
        self.player = Player(0, self.display_height/2)
        self.missiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.animations = {0: BlueExplosion(), 1: RedExplosion()}
        self.animation_type = 0

    def update_enemies(self):
        if self.frames_count % 180 == 0:
            self.enemies.add(ShipFactory.create())
        for enemy in self.enemies:
            missile = enemy.attack()
            if missile is not None:
                self.missiles.add(missile)
            enemy.time_shooting()
            collisions = spritecollide(enemy, self.missiles, True)
            if collisions:
                for missile in collisions:
                    enemy.health -= missile.damage
            enemy.move()
            if enemy.health < 0:
                self.animation_type = random.randint(0, 1)
                self.animations[self.animation_type].change_postion(enemy.rect.x - 40, enemy.rect.y - 30)
                self.enemies.remove(enemy)

    def update_shield(self):
        if self.frames_count % 800 == 0:
            x = random.randint(30, 300)
            self.shield = Shield(x, -50)
        if self.shield is not None:
            self.shield.move()
            player_collision = collide_rect(self.player, self.shield)
            if player_collision:
                self.shield.activate()
                self.shield.update(self.player.rect.x - 15, self.player.rect.y - 10)
                if self.shield.deactivate():
                    self.shield = None

    def update_missiles(self):
        for missile in self.missiles:
            missile.move()

    def update_box(self):
        if self.frames_count % 720 == 0:
            x = random.randint(30, 300)
            self.box = Box(x, -50)
        if self.box is not None:
            self.box.move()
            if collide_rect(self.player, self.box):
                self.box = None

    def update_player(self):
        self.player.move()
        self.player.time_shooting()
        missile = self.player.shoot()
        if missile is not None:
            self.missiles.add(missile)
        missiles_collisions = spritecollide(self.player, self.missiles, True)
        if missiles_collisions and self.shield is None:
            for missile in missiles_collisions:
                self.player.health -= missile.damage
        enemy_collisions = spritecollide(self.player, self.enemies, True)
        if enemy_collisions and self.shield is None:
            self.player.health = 0
        else:
            for enemy in enemy_collisions:
                enemy.health = 0

    def update(self):
        self.update_player()
        self.update_missiles()
        self.update_enemies()
        self.update_box()
        self.update_shield()

    def draw(self):
        self.missiles.draw(self.main_screen)
        self.enemies.draw(self.main_screen)
        self.main_screen.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        if self.box is not None:
            self.main_screen.blit(self.box.image, (self.box.rect.x, self.box.rect.y))
        if self.shield is not None:
            self.main_screen.blit(self.shield.image, (self.shield.rect.x, self.shield.rect.y))
        self.animations[self.animation_type].show(self.main_screen)
