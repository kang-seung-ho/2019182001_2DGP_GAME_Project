from pico2d import *
import game_framework
import game_world

class Fortress:
    def __init__(self, x=1280, y=720):
        self.image = load_image('fortress.png')
        self.x, self.y = x, y
        self.cnt = 0
        self.hp = 300

    def draw(self):
        self.image.draw(self.x+10, self.y, 120, 120)

    def update(self):
        if self.hp <= 0 :
            game_world.remove_objects(self)

