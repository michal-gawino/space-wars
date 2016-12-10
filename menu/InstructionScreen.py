

class InstructionScreen:
    def __init__(self):
        self.instructions = {'movement.png': (10, 50), 'shooting.png': (10, 370), 'mov1.png': (0, 120), 'mov2.png': (0, 220),
                             'sh1.png': (50, 425), 'sh2.png': (50, 480), 'back.png': (550, 500)}
        self.weapons = [('red_laser.png', (290, 440)), ('blue_laser.png', (145, 485)), ('blue_laser.png', (145, 505)),
                        ('missile.png', (140, 535))]