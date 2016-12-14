import math


class Strategy:

    def execute(self):
        raise NotImplementedError()

class MovementStrategy(Strategy):

    def execute(x, y, start_y):
        return x-2,  30 * math.sin(x * 0.025) + start_y


