from image import Image


class Button(Image):
    _LINE_IMAGE_PATH = 'blue_laser.png'

    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)
        self.line = Image(self.x, self.y + self.height, self._LINE_IMAGE_PATH)
        self.line.scale(self.width, 3)

    def highlight(self, screen):
        self.line.show(screen)
