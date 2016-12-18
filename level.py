from image import Image


class Level:
    _LEVEL1_IMAGE_PATH = 'menu/level1.png'
    _LEVEL2_IMAGE_PATH = 'menu/level2.png'
    _LEVEL3_IMAGE_PATH = 'menu/level3.png'

    def __init__(self):
        self.current_level = 1
        self.levels = {1: 14, 2: 21, 3: 28}
        self.images = [Image(250, 100, self._LEVEL1_IMAGE_PATH), Image(250, 100, self._LEVEL2_IMAGE_PATH),
                       Image(250, 100, self._LEVEL3_IMAGE_PATH)]
        self.duration = 180

    def show(self, screen):
        if self.duration > 0:
            self.images[self.current_level - 1].show(screen)
            self.duration -= 1

    def update(self):
        if self.levels[self.current_level] == 0 and self.current_level < 3:
            self.current_level += 1
            self.duration = 180
