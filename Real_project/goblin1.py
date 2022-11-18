from pico2d import *
import game_world
import game_framework
import random
import game_over

TIME_PER_ACTION = 0.3
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


PIXEL_PER_METER = (10.0/0.2)
RUN_SPEED_KMPH = 2.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)


power = None
hp = 240

class goblin:
    def __init__(self):
        global power, hp

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
        self.hp = 240
        self.hp = hp
        self.frame = 0
        power = 40
        self.power = 40

        self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
        # self.state = 'COLLIDE'
        self.state = 'RUN'

    def update(self):
        self.frame = self.frame = (self.frame + random.randint(0, 8) + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        if self.state == 'RUN':
            self.x += (-1) * self.RUN_SPEED_PPS * game_framework.frame_time
            self.RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        if self.x <= 20:
            game_framework.change_state(game_over)

        if self.hp <= 0:
            game_world.remove_objects(self)
        self.hp = hp

    def draw(self):
        self.image.clip_draw(int(self.frame) * 64, 64 * 1, 64, 64, self.x, self.y, 120, 120)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 33, self.y - 45, self.x + 37, self.y + 53

    def handle_collision(self, other, group):
        if group == 'boy:goblin_crowd':
            self.RUN_SPEED_PPS = 0

