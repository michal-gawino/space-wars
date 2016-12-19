import math


class Strategy:

    def execute(x, y, speed, start_y):
        raise NotImplementedError()


class SineMovement(Strategy):

    def execute(x, y, speed, start_y):
        return x - speed, 25 * math.sin(x * 0.02) + start_y


class CosineMovement(Strategy):

    def execute(x, y, speed, start_y):
        return x - speed, 35 * math.cos(x * 0.011) + start_y

class LinearMovement(Strategy):

    def execute(x, y, speed, start_y):
        return x - abs(speed), y - speed
