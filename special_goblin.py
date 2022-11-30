from pico2d import *

import game_world
import game_framework
import random
import game_over_state

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


PIXEL_PER_METER = (10.0/0.2)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)

class Special_goblin:
    def __init__(self):

        self.randnum = random.randint(1, 10000) % 8
        if self.randnum == 0:
            self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER) * 2
        else:
            self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.image = load_image('resources/sprite_sheet/goblinsword_surprize.png')
        self.attacked = load_image('resources/sprite_sheet/goblinsword_attacked.png')
        self.x = random.randint(800, 1000)
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


        self.state = 'RUN'


    def update(self):
        self.frame = self.frame = (self.frame + random.randint(0, 8) + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        self.x += (-1) * self.RUN_SPEED_PPS * game_framework.frame_time
        if self.randnum == 0:
            self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER) * 2
        else:
            self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        if self.x <= 20:
            game_framework.change_state(game_over_state)

        if self.hp <= 0:
            game_world.second_stage_special_goblin_cnt -= 1
            game_world.coin += 15
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
        if group == 'boy:special_goblin':
            self.RUN_SPEED_PPS = 0
        elif group == 'fortress1:special_goblin':
            self.RUN_SPEED_PPS = 0
        elif group == 'fortress2:special_goblin':
            self.RUN_SPEED_PPS = 0
        elif group == 'tree1:special_goblin':
            self.RUN_SPEED_PPS = 0
        elif group == 'tree2:special_goblin':
            self.RUN_SPEED_PPS = 0
        elif group == 'my_bullet:special_goblin':
            self.state = 'ATTACKED'
            self.hp -= game_world.character_power
        elif group == 'my_cannon:special_goblin':
            self.RUN_SPEED_PPS = 0
        elif group == 'cannon_bullet:special_goblin':
            self.state = 'ATTACKED'
            self.hp -= 60

