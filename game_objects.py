import pygame


class GameObject(pygame.sprite.Sprite):
    _IMAGE_PATH = None

    def __init__(self, x, y):
        super().__init__()
        assert self._IMAGE_PATH is not None, 'Image path not specified'
        self.image = pygame.image.load(self._IMAGE_PATH).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        raise NotImplementedError()