from pico2d import *
import random

class RUN:
    def enter(self, event):  # IDLE에서 run으로 들어올때 어떤 키를 눌렀기 때문에 run에 들어왔는지 판단
        pass

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x -= 1

        pass

    def draw(self):
        if self.hp >= 0:
            self.image.clip_draw(self.frame*64, 64*1, 64, 64, self.x, self.y, 120, 120)
        else:
            pass
            # del self

class monster:

    def __init__(self):
        rand_x = random.randint(1300, 1700)
        rand_y = random.randint(0, 4 + 1)
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

        self.hp = 300

        self.x, self.y = rand_x, monster_y
        self.frame = random.randint(0, 8)
        self.image = load_image('goblinsword.png')

    def update(self):
        RUN.do(self)
    def draw(self):
        RUN.draw(self)