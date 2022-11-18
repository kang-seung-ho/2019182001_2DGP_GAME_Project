from pico2d import *
import game_framework
import game_world

class Tree:
    def __init__(self, x=1280, y=720):
        self.image = load_image('tree_spring.png')
        self.x, self.y = x, y
        self.cnt = 0
        self.hp = 300.0

    def draw(self):
        self.image.draw(self.x, self.y, 115, 115)
        draw_rectangle(*self.get_bb())

    def update(self):
        if self.hp <= 0:
            game_world.remove_objects(self)

    def get_bb(self):
        return self.x-47, self.y-55, self.x+48, self.y+57


    def handle_collision(self, other, group):
        if group == 'tree1:goblin_crowd':
            self.hp -= 0.7
        if group == 'tree2:goblin_crowd':
            self.hp -= 0.7