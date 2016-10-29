import pygame


class GameObjects(pygame.sprite.Sprite):
    objects = pygame.sprite.Group()

    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        GameObjects.objects.add(self)
        self.image = pygame.image.load('images/' + image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y