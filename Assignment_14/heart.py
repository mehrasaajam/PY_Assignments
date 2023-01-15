
import arcade

class Heart(arcade.Sprite):
    def __init__(self, a, game):
        super().__init__("heart.png")
        self.center_x = a
        self.center_y = 0.05 * game.height
        self.width = 0.03 * game.width
        self.height = 0.04 * game.height
        self.change_x = 0
        self.change_y = 0