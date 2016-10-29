from box import *
from enemy import *


class Player(GameObjects):

    def __init__(self, x, y, image):
        GameObjects.__init__(self, x, y, image)
        self.speed = 3
        self.health = 100
        self.missiles = 3
        self.blue_laser = 12
        self.timer = 25
        self.score = 0

    def motion(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.y - 3 > 30:
            self.rect.y -= self.speed
        elif keys[pygame.K_DOWN] and self.rect.y + 3 < 600 - self.image.get_height():
            self.rect.y += self.speed
        elif keys[pygame.K_LEFT] and self.rect.x + 3 > 0:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.timer == 25:
            if keys[pygame.K_SPACE]:
                Missile(self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height()/2 - 8, 'red_laser.png', 0)
                self.timer = 0
            elif keys[pygame.K_2] and self.missiles > 0:
                Missile(self.rect.x + self.image.get_width(), self.rect.y + self.image.get_height()/2 - 8, 'missile.png', 2)
                self.missiles -= 1
                self.timer = 0
            elif keys[pygame.K_1] and self.blue_laser > 0:
                Missile(self.rect.x + 80, self.rect.y + 10, 'blue_laser.png', 1)
                Missile(self.rect.x + 80, self.rect.y + 55, 'blue_laser.png', 1)
                self.blue_laser -= 1
                self.timer = 0

    def time_shooting(self):
        if self.timer < 25:
            self.timer += 1

    def detect_missiles_collisions(self):
        collisions = pygame.sprite.spritecollide(self, Missile.missiles, True)
        if collisions:
            for missile in collisions:
                if missile.missile_type in [3, 4, 5]:
                    self.health -= missile.damage

    def detect_enemy_collisions(self):
        collisions = pygame.sprite.spritecollide(self, Enemy.enemies, True)
        if collisions:
            self.health -= 100

    def detect_box_collisions(self):
        collisions = pygame.sprite.spritecollide(self, Box.boxes, True)
        if collisions:
            self.missiles += random.randint(2, 3)
            self.blue_laser += random.randint(6, 7)
            health = random.randint(5, 15)
            if self.health + health < 100:
                self.health += health
            else:
                self.health = 100

    def detect_collisions(self):
        self.detect_missiles_collisions()
        self.detect_enemy_collisions()
        self.detect_box_collisions()