from pico2d import *
import game_framework
import game_world

class Fortress:
    def __init__(self, x=1280, y=720):
        self.image = load_image('resources/stage_object/fortress.png')
        self.x, self.y = x, y
        self.cnt = 0
        self.hp = 500.0

    def draw(self):
        self.image.draw(self.x, self.y, 120, 120)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.hp <= 0:
            game_world.remove_objects(self)
            game_world.remove_collision_object(self)

    def get_bb(self):
        return self.x-47, self.y-60, self.x+48, self.y+60


    def handle_collision(self, other, group):
        if group == 'fortress1:goblin_crowd':
            self.hp -= 0.7
        elif group == 'fortress2:goblin_crowd':
            self.hp -= 0.7
        elif group == 'fortress1:boss':
            self.hp -= 1
        elif group == 'fortress2:boss':
            self.hp -= 1
        elif group == 'fortress1:special_goblin':
            self.hp -= 0.9
        elif group == 'fortress2:special_goblin':
            self.hp -= 0.9
        elif group == 'fortress3:special_goblin':
            self.hp -= 0.9