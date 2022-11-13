from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('map1_spring_temp.png')

    def draw(self):
        self.image.draw(1280//2, 720//2)