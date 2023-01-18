
import random
import time
import arcade
from spaceship_friend import Spaceship_friend
from spaceship_enemy import Spaceship_enemy
from bullet import Bullet
from heart import Heart


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=800, height=600, title="Interstellar 2023")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.background_finish = arcade.load_texture("game_over.png")
        self.me = Spaceship_friend(self, "Mehrasa")
        self.enemy_list = []
        self.seconds = time.time()
        self.gap = 3
        self.score = 0
        self.state = 1
        self.enemy_sound = arcade.load_sound(":resources:sounds/hurt3.wav")
        self.game_over_sound = arcade.load_sound(":resources:sounds/gameover3.wav")
        self.num_of_heart = 3
        self.heart_list = []
        for i in range(3):
            a = (1-(0.05*(i+1)))*self.width
            heart = Heart(a, self)
            self.heart_list.append(heart)
            

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.me.draw()

        for enemy in self.enemy_list:
            enemy.draw()

        for bullet in self.me.bullet_list:
            bullet.draw()

        for heart in self.heart_list:
            heart.draw()

        arcade.draw_text(f"Score: {self.score}", 0.05*self.width, 0.05*self.height, arcade.color.WHITE)
        
        if self.num_of_heart == 0 or self.state == 0: 
            arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background_finish)
            arcade.play_sound(self.game_over_sound)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.me.change_x = 1
        elif symbol == arcade.key.LEFT:
            self.me.change_x = -1
        elif symbol == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol, modifiers):
        self.me.change_x = 0

    def on_update(self, delta_time):

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me, enemy):
                self.state = 0

        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy, bullet):
                    arcade.play_sound(self.enemy_sound)
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                    self.score += 1

        self.me.move()

        for enemy in self.enemy_list:
            enemy.move(self.score)

        for bullet in self.me.bullet_list:
            bullet.move()
            if bullet.center_y > self.height:
                self.me.bullet_list.remove(bullet)

        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.enemy_list.remove(enemy)
                self.num_of_heart -= 1
                if self.num_of_heart == 2:
                    del self.heart_list[2]
                elif self.num_of_heart == 1:
                    del self.heart_list[1]
                elif self.num_of_heart == 0:
                    del self.heart_list[0]  

        if int(time.time()-self.seconds) == self.gap:
            self.gap += 3
            self.new_enemy_list = Spaceship_enemy(self.width, self.height)
            self.enemy_list.append(self.new_enemy_list)
      

window = Game()
arcade.run()
