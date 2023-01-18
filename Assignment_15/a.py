
import random
import arcade

class Fruit(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = random.randint(self.width/2, game.width-(self.width/2))
        self.center_y = random.randint(self.height/2, game.height-(self.height/2))
        self.change_x = 0
        self.change_y = 0

class Apple(Fruit):
    def __init__(self, game):
        super().__init__("apple.png")

class Pear(Fruit):
    def __init__(self):
        super().__init__("pear.png")
        
class Poop(Fruit):
    def __init__(self):
        super().__init__("poop.png")
        

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.color = arcade.color.GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color)

        for part in self.body:
            arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, self.color)

    def move(self):
        self.body.append({'x':self.center_x, 'y':self.center_y}) 
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        

    def eat(self):
        ...


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Super Snake ")
        arcade.set_background_color(arcade.color.KHAKI)
        self.apple = Apple(self)
        self.pear = Pear(self)
        self.poop = Poop(self)
        self.snake = Snake(self)

    def on_draw(self):
        arcade.start_render()
        self.apple.draw()
        self.pear.draw()
        self.poop.draw()
        self.snake.draw()

        arcade.draw_text(f"Score: {self.snake.score}", 0.05*self.width, 0.05*self.height, arcade.color.BLACK)

        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.apple):
            del apple
            self.score += 1
            self.apple = Apple(self)
        elif arcade.check_for_collision(self.snake, self.pear):
            del pear
            self.score += 2
            self.pear = Pear(self)
        elif arcade.check_for_collision(self.snake, self.poop):
            del poop
            self.score -= 1
            self.poop = Poop(self)

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        


if __name__ == "__main__":
    game = Game()
    arcade.run()