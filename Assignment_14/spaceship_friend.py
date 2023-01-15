
import arcade
from bullet import Bullet

class Spaceship_friend(arcade.Sprite):
    def __init__(self, game, name):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = game.width // 2
        self.center_y = 0.05 * game.height
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.name = name
        self.speed = 4
        self.game_width = game.width
        self.bullet_list = []

    def move(self):
        if self.change_x == 1:
            if self.center_x < self.game_width:
                self.center_x += self.speed
        elif self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed

    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)
