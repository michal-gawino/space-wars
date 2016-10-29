import random
import math
from missile import *
import pygame


class Enemy(GameObjects):
    enemies = pygame.sprite.Group()

    def __init__(self, x, y, image, enemy_type):
        GameObjects.__init__(self, x, y, image)
        Enemy.enemies.add(self)
        self.start_pos = y
        self.speed = -1
        self.timer = 180
        self.amplitude = random.randint(1, 15)
        self.type = {0: [100, 0], 1: [125, 1], 2: [145, 2]}
        self.health, self.attack_type = self.type[enemy_type]

    def motion(self):
        self.rect.x += self.speed
        self.rect.y = self.amplitude * math.sin(self.rect.x * 0.019) + self.start_pos

    def attack(self):
        if self.timer == 180:
            if self.attack_type == 0:
                Missile(self.rect.x - 34, self.rect.y + 10, 'mine.png', 3)
            elif self.attack_type == 1:
                Missile(self.rect.x - 32, self.rect.y + 10, 'attack2.png', 4)
            elif self.attack_type == 2:
                Missile(self.rect.x - 52, self.rect.y + 10, 'green_laser.png', 5)
            self.timer = 0

    def time_shooting(self):
        if self.timer < 180:
            self.timer += 1

    @staticmethod
    def spawn(total_frames):
        if total_frames % 180 == 0:
            y = random.randint(100, 500)
            enemy_type = random.randint(0, 2)
            if enemy_type == 0:
                Enemy(700, y, 'alien.png', 0)
            elif enemy_type == 1:
                Enemy(700, y, 'alien2.png', 1)
            else:
                Enemy(700, y, 'alien3.png', 2)

    @staticmethod
    def movement():
        for enemy in Enemy.enemies:
            enemy.motion()
            enemy.attack()
            enemy.time_shooting()

    @staticmethod
    def destroy(player):
        for enemy in Enemy.enemies:
            if enemy.health <= 0:
                player.score += (enemy.attack_type + 1) * 10
                Enemy.enemies.remove(enemy)
                GameObjects.objects.remove(enemy)

    @staticmethod
    def detect_collisions():
        for enemy in Enemy.enemies:
            collisions = pygame.sprite.spritecollide(enemy, Missile.missiles, True)
            if collisions:
                for missile in collisions:
                    if missile.missile_type in [0, 1, 2]:
                        enemy.health -= missile.damage

    @staticmethod
    def detect_border_collision(player):
        for enemy in Enemy.enemies:
            if enemy.rect.x < player.rect.x:
                return True
