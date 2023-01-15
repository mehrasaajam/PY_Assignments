
import random
import arcade

class Spaceship_enemy(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = random.randint(0, w)
        self.center_y = 1.05 * h
        self.width = 50
        self.height = 50
        self.angle = 180
        self.speed = 2

    def move(self, score):
        if score <= 5:
            self.center_y -= self.speed
        elif score > 5 and score <= 15:
            self.center_y -= (1.2 * self.speed)
        elif score > 15 and score <= 25:
            self.center_y -= (1.5 * self.speed)
        elif score > 25:
            self.center_y -= (2* self.speed)
        