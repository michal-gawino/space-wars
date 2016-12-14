import random
import pygame


class Effect:

    def __init__(self, n):
        self.stars = [[random.randint(0, 800), random.randint(0, 600)] for _ in range(n)]

    def draw(self, screen):
        for star in self.stars:
            pygame.draw.line(screen, (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            star[0] -= 0.7
            if star[0] < 0:
                star[0] = 800
                star[1] = random.randint(0, 600)
