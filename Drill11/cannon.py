from pico2d import *
import game_framework
import game_world

class Cannon:
    def __init__(self, x=1280, y=720):
        self.image = load_image('cannon.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x+10, self.y, 100, 100)

    def update(self):
        pass