from pico2d import *
import game_framework
import game_world
from cannon_bullet import can_bullet
import time


class Cannon:
    def __init__(self, x=1280, y=720):
        self.image = load_image('cannon.png')
        self.x, self.y = x, y
        self.start_time = time.time()
        self.cnt = 0

    def draw(self):
        self.image.draw(self.x+10, self.y, 100, 100)

    def update(self):
        self.end_time = time.time()
        self.delay_time = (self.start_time - self.end_time)
        self.cnt += 1
        if self.cnt % 300 == 0:
            my_can_bullet = can_bullet(self.x, self.y, 1.5)
            game_world.add_object(my_can_bullet, 1)