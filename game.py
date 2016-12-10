import os
import random
import pygame
from box import Box
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

    def draw(self):
        self.missiles.draw(self.game_display)
        self.enemies.draw(self.game_display)
        self.game_display.blit(self.player.image, (self.player.rect.x, self.player.rect.y))
        if self.box is not None:
            self.game_display.blit(self.box.image, (self.box.rect.x, self.box.rect.y))

    def run(self):
        pygame.display.set_caption('Space Wars')
        pygame.mouse.set_visible(True)
        intro = True
        pygame.init()

    def game_loop(self):
        clock = pygame.time.Clock()
        final_background = pygame.image.load('images/final_screen.png').convert_alpha()
        pygame.mouse.set_visible(False)
        replay = False
        self.player = Player(0, self.display_height/2)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.frames += 1
            if self.player.health <= 0:
                final_screen = True
                while final_screen:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            final_screen = False
                            run = False
                        elif event.type == pygame.KEYDOWN:
                            final_screen = False
                            run = False
                            replay = True
                    self.game_display.blit(final_background, (0, 0))
                    pygame.display.update()
            else:
                self.update_enemies()
                self.update_missiles()
                self.update_box()
                self.update_player()
                self.game_display.fill((0, 0, 0))
                self.draw()
                pygame.display.update()
                clock.tick(60)
        if replay:
            self.run()