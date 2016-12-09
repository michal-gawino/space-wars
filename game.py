import os
import random
import pygame
from box import Box
from effect import Effect
from missile import Missile
from menu import Menu
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

    def run(self):
        pygame.display.set_caption('Space Wars')
        pygame.mouse.set_visible(True)
        stars = Effect(25)
        stars.generate_stars()
        intro = True
        pygame.init()
        menu = Menu()
        game = False
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False

            menu.create_menu(self.game_display)
            stars.apply(self.game_display)
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 604 > mouse[0] > 200 and 322 > mouse[1] > 280:
                menu.highlight(self.game_display, (180, 330), 450)
                if click[0]:
                    intro = False
                    game = True
            elif 596 > mouse[0] > 200 and 402 > mouse[1] > 360:
                menu.highlight(self.game_display, (180, 410), 450)
                if click[0]:
                    instruction = True
                    while instruction:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                instruction = False
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if 675 > mouse[0] > 550 and 530 > mouse[1] > 500:
                            if click[0]:
                                instruction = False
                        menu.show_instruction(self.game_display)
                        stars.apply(self.game_display)
                        pygame.display.update()
            elif 475 > mouse[0] > 330 and 482 > mouse[1] > 440:
                menu.highlight(self.game_display, (325, 490), 155)
                if click[0]:
                    intro = False
            pygame.display.update()
        if game:
            self.game_loop()

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