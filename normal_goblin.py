from pico2d import *

import character
import game_world
import game_framework
import random
import game_over_state
from character import Character

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


PIXEL_PER_METER = (10.0/0.2)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)


power = None

class Normal_goblin:
    def __init__(self):
        global power, hp

        self.image = load_image('resources/sprite_sheet/goblinsword.png')
        self.attacked = load_image('resources/sprite_sheet/goblinsword_attacked.png')
        self.x = random.randint(1300, 2200)
        rand_x = random.randint(200, 400)
        self.x += rand_x
        rand_y = random.randint(0, 4+1)
        monster_y = 180
        if rand_y == 0:
            monster_y = 650
        elif rand_y == 1:
            monster_y = 530
        elif rand_y == 2:
            monster_y = 410
        elif rand_y == 3:
            monster_y = 300
        elif rand_y == 4:
            monster_y = 180

        rand_y = random.randint(0, 4 + 1)
        if monster_y == 180:
            if rand_y == 0:
                monster_y = 650
            elif rand_y == 1:
                monster_y = 530
            elif rand_y == 2:
                monster_y = 410
            elif rand_y == 3:
                monster_y = 300

        self.y = monster_y
        self.hp = 200
        self.frame = 0
        self.power = 40

        self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        self.state = 'RUN'


    def update(self):
        self.frame = self.frame = (self.frame + random.randint(0, 8) + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += (-1) * self.RUN_SPEED_PPS * game_framework.frame_time
        self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        if self.x <= 20:
            game_framework.change_state(game_over_state)

        if self.hp <= 0:
            game_world.remove_objects(self)

    def draw(self):
        if self.state == 'RUN':
            self.image.clip_draw(int(self.frame) * 64, 64 * 1, 64, 64, self.x, self.y, 120, 120)
        elif self.state == 'ATTACKED':
            self.attacked.clip_draw(int(self.frame) * 64, 64 * 1, 64, 64, self.x, self.y, 120, 120)
            self.state = 'RUN'

        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 33, self.y - 45, self.x + 37, self.y + 53

    def handle_collision(self, other, group):
        if group == 'boy:goblin_crowd':
            self.RUN_SPEED_PPS = 0
        elif group == 'fortress1:goblin_crowd':
            self.RUN_SPEED_PPS = 0
        elif group == 'fortress2:goblin_crowd':
            self.RUN_SPEED_PPS = 0
        elif group == 'tree1:goblin_crowd':
            self.RUN_SPEED_PPS = 0
        elif group == 'tree2:goblin_crowd':
            self.RUN_SPEED_PPS = 0
        elif group == 'my_bullet:goblin_crowd':
            self.state = 'ATTACKED'
            self.hp -= 40
        elif group == 'my_cannon:goblin_crowd':
            self.RUN_SPEED_PPS = 0
        elif group == 'cannon_bullet:goblin_crowd':
            self.state = 'ATTACKED'
            self.hp -= 60

