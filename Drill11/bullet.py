from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x=800, y=300, velocity=1):
        if Ball.image == None:
            Ball.image = load_image('bullet.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x + 5, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 710:
            game_world.remove_objects(self)
