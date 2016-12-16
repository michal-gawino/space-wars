import math


class Strategy:

    def execute(self):
        raise NotImplementedError()

class MovementStrategy(Strategy):

    def execute(x, y, speed, start_y):
        return x-speed, 25 * math.sin(x * 0.023) + start_y

