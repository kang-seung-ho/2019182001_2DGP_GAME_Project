from pico2d import *

import character
import game_world
import game_framework
import random
import game_over_state

TIME_PER_ACTION = 0.1
ACTION_PER_TIME = 2.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


PIXEL_PER_METER = (20.0/0.2)
RUN_SPEED_KMPH = 1.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)


power = None

class Boss_monster:
    def __init__(self):
        global power, hp

        self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.image = load_image('resources/sprite_sheet/first_boss_monster1.png')
        # self.attacked = load_image('resources/sprite_sheet/goblinsword_attacked.png')
        self.x = random.randint(1300, 2000)

        self.x = 1400
        self.y = 720//2
        self.hp = 2000
        self.frame = 0
        self.power = 40


        self.state = 'RUN'


    def update(self):
        self.frame = self.frame = (self.frame + random.randint(0, 6) + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
        self.x += (-1) * self.RUN_SPEED_PPS * game_framework.frame_time

        self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        if self.x <= 20:
            game_framework.change_state(game_over_state)

        if self.hp <= 0:
            game_world.first_boss_cnt -= 1
            game_world.coin += 10
            game_world.remove_objects(self)

    def draw(self):
        if self.state == 'RUN':
            self.image.clip_draw(int(self.frame) * 184, 226 * 1, 184, 184, self.x, self.y, 200, 200)
        # elif self.state == 'ATTACKED':
        #     self.attacked.clip_draw(int(self.frame) * 64, 64 * 1, 64, 64, self.x, self.y, 120, 120)
        #     self.state = 'RUN'


        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 92, self.y - 75, self.x + 85, self.y + 55

    def handle_collision(self, other, group):
        if group == 'boy:boss':
            self.RUN_SPEED_PPS = 0
        elif group == 'fortress1:boss':
            self.RUN_SPEED_PPS = 0
        elif group == 'fortress2:boss':
            self.RUN_SPEED_PPS = 0
        elif group == 'tree1:boss':
            self.RUN_SPEED_PPS = 0
        elif group == 'tree2:boss':
            self.RUN_SPEED_PPS = 0
        elif group == 'my_bullet:boss':
            # self.state = 'ATTACKED'
            self.hp -= game_world.character_power
        elif group == 'my_cannon:boss':
            self.RUN_SPEED_PPS = 0
        elif group == 'cannon_bullet:boss':
            self.state = 'ATTACKED'
            self.hp -= 60

