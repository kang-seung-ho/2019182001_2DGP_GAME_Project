from pico2d import *
import game_world
import game_framework
import random

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 15.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class RUN:
    def enter(self):
        pass
    def exit(self):
        pass
    def do(self):
        self.frame = self.frame = (self.frame + random.randint(0, 8) + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += (-1) * RUN_SPEED_PPS * game_framework.frame_time

        if self.x <= 20:
            self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*64, 64*1, 64, 64, self.x, self.y, 120, 120)

class goblin:
    def __init__(self):
        self.image = load_image('goblinsword.png')
        self.x = random.randint(1300, 1700)
        rand_y = random.randint(0, 4+1)
        monster_y = 190
        if rand_y == 0:
            monster_y = 650
        elif rand_y == 1:
            monster_y = 530
        elif rand_y == 2:
            monster_y = 410
        elif rand_y == 3:
            monster_y = 300
        elif rand_y == 4:
            monster_y = 190
        self.y = monster_y
        self.hp = 300
        self.frame = 0
        self.cur_state = RUN

    def update(self):
        self.cur_state.do(self)

    def draw(self):
        self.RUN.draw(self)