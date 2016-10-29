import random
import pygame


class Effect:

    def __init__(self, n):
        self.n = n
        self.stars = []

    def generate_stars(self):
        self.stars = [[random.randint(0, 800), random.randint(0, 600)] for x in range(self.n)]

    def apply(self, screen):
        for star in self.stars:
            pygame.draw.line(screen, (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            star[0] -= 1
            if star[0] < 0:
                star[0] = 800
                star[1] = random.randint(0, 600)