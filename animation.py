import pygame
from menu.image import Image


class Animation(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frame = -1

    def change_position(self, x, y):
        self.frame = 0
        for image in self.images:
            image.rect.x, image.rect.y = x, y

    def show(self, screen):
        if self.frame < len(self.images) - 1:
            self.frame += 1
            self.image = self.images[self.frame].image
            screen.blit(self.image, (self.images[self.frame].x, self.images[self.frame].y))


class BlueExplosion(Animation):
    def __init__(self):
        super().__init__()
        self.images = [Image(-100, 0, 'animations/blue_explosion/1.png'), Image(-100, 0, 'animations/blue_explosion/2.png'),
                       Image(-100, 0, 'animations/blue_explosion/3.png'), Image(-100, 0, 'animations/blue_explosion/4.png'),
                       Image(-100, 0, 'animations/blue_explosion/5.png'), Image(-100, 0, 'animations/blue_explosion/6.png'),
                       Image(-100, 0, 'animations/blue_explosion/7.png'), Image(-100, 0, 'animations/blue_explosion/8.png'),
                       Image(-100, 0, 'animations/blue_explosion/9.png'), Image(-100, 0, 'animations/blue_explosion/10.png'),
                       Image(-100, 0, 'animations/blue_explosion/11.png'), Image(-100, 0, 'animations/blue_explosion/12.png')]

class RedExplosion(Animation):
    def __init__(self):
        super().__init__()
        self.images = [Image(0, 0, 'animations/red_explosion/1.png'), Image(0, 0, 'animations/red_explosion/2.png'),
                       Image(0, 0, 'animations/red_explosion/3.png'), Image(0, 0, 'animations/red_explosion/4.png'),
                       Image(0, 0, 'animations/red_explosion/5.png'), Image(0, 0, 'animations/red_explosion/6.png'),
                       Image(0, 0, 'animations/red_explosion/7.png'), Image(0, 0, 'animations/red_explosion/8.png'),
                       Image(0, 0, 'animations/red_explosion/9.png'), Image(0, 0, 'animations/red_explosion/10.png'),
                       Image(0, 0, 'animations/red_explosion/11.png'), Image(0, 0, 'animations/red_explosion/12.png'),
                       Image(0, 0, 'animations/red_explosion/13.png'), Image(0, 0, 'animations/red_explosion/14.png'),
                       Image(0, 0, 'animations/red_explosion/15.png'), Image(0, 0, 'animations/red_explosion/16.png'),
                       Image(0, 0, 'animations/red_explosion/17.png'), Image(0, 0, 'animations/red_explosion/18.png'),
                       Image(0, 0, 'animations/red_explosion/19.png')]

