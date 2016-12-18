import pygame
from image import Image


class TopBar:

    def __init__(self):
        self.health_image = Image(44, 17, 'health.png')
        self.images = [Image(20, 5, 'health_bar.png'), Image(220, 17, 'missile_small.png'),
                       Image(330, 17, 'blue_laser.png'), Image(330, 34, 'blue_laser.png')]
        self.font = pygame.font.SysFont("arial", 25)

    def draw(self, screen, missile_count, laser_count, score):
        self.health_image.show(screen)
        missiles_label = self.font.render(str(missile_count), 1, (255, 255, 255))
        laser_label = self.font.render(str(laser_count), 1, (255, 255, 255))
        score_label = self.font.render('Score : '+str(score), 1, (255, 255, 255))
        screen.blit(missiles_label, (250, 17))
        screen.blit(laser_label, (365, 17))
        screen.blit(score_label, (650, 17))
        for image in self.images:
            image.show(screen)

    def update(self, player_health):
        if player_health > 0:
            self.health_image.scale(player_health, 17)
