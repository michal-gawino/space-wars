from image import Image


class TopBar:

    def __init__(self):
        self.health_image = Image(44, 17, 'health.png')
        self.images = [Image(20, 5, 'health_bar.png'), Image(250, 17, 'missile_small.png'),
                       Image(380, 17, 'blue_laser.png'), Image(380, 34, 'blue_laser.png')]

    def draw(self, screen):
        self.health_image.show(screen)
        for image in self.images:
            image.show(screen)

    def update(self, player_health):
        if player_health > 0:
            self.health_image.scale(player_health, 17)
