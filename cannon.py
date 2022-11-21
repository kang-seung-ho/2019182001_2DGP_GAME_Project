from pico2d import *
import game_framework
import game_world
from cannon_bullet import Can_bullet
import time


class Cannon:
    def __init__(self, x=1280, y=720):
        self.image = load_image('resources/weapon/cannon.png')
        self.x, self.y = x, y
        self.start_time = time.time()
        self.cnt = 0
        self.hp = 800

    def draw(self):
        self.image.draw(self.x+10, self.y, 100, 100)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.end_time = time.time()
        self.delay_time = (self.start_time - self.end_time)
        self.cnt += 1
        if self.cnt % 300 == 0:
            cannon_bullet = Can_bullet(self.x, self.y, 1.5)
            game_world.add_object(cannon_bullet, 1)
            game_world.add_collision_pairs(cannon_bullet, None, 'cannon_bullet:goblin_crowd')
        if self.hp <= 0:
            game_world.remove_objects(self)

    def get_bb(self):
        return self.x - 43, self.y - 47, self.x + 59, self.y + 38

    def handle_collision(self, other, group):
        if group == 'my_cannon:goblin_crowd':
            self.hp -= 1
