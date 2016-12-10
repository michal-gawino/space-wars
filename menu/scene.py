from menu.FinalScreen import FinalScreen
from menu.game_screen import GameScreen
from menu.instruction_screen import InstructionScreen
from menu.menu_screen import MenuScreen


class Scene:

    def __init__(self):
        self.current = 'menu';
        self.scenes = {'menu': MenuScreen(), 'instruction': InstructionScreen(), 'game': GameScreen(),
                       'final': FinalScreen()}

    def change(self, name):
        self.current = name

    def draw(self, screen):
        self.scenes[self.current].draw(screen)
