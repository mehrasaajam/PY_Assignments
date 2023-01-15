
import arcade

class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y + host.height
        self.speed = 3
        self.change_x = 0
        self.change_y = 3
        self.bullet_sound = arcade.load_sound(":resources:sounds/laser2.wav")

    def move(self):
        arcade.play_sound(self.bullet_sound)
        self.center_y += self.speed
        