
import random
import arcade

class Green_fish(arcade.Sprite):
    def __init__(self, game, name):
        super().__init__(":resources:images/enemies/fishGreen.png")
        self.center_x = 0.05 * game.width
        self.center_y = game.height// 2
        self.angle = 180
        self.width = 60
        self.height = 60
        self.name = name
        self.speed = 15

class Pink_fish(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__(":resources:images/enemies/fishPink.png")
        self.center_x = 0.95 * w
        self.center_y = random.randint(0, h)
        self.width = 60
        self.height = 60
        self.speed = 3
        

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Aquarium 2023")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(":resources:images/tiles/water.png")
        self.me = Green_fish(self, "Mehrasa")
        self.enemy = Pink_fish(self.width, self.height)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()
        self.enemy.draw()

    def on_key_press(self, symbol, modifiers):
        print(symbol)
        if symbol == 97:
            self.me.center_y -= self.me.speed
        elif symbol == 100:
            self.me.center_y += self.me.speed
    
    def on_update(self, delta_time):
         self.enemy.center_x -= self.enemy.speed
        
window = Game()
arcade.run()
