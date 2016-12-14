import math


class Strategy:

    def execute(self):
        raise NotImplementedError()

class MovementStrategy(Strategy):

    def execute(x, y, speed, start_y):
        return x-speed, 30 * math.sin(x * 0.025) + start_y


