from pico2d import *
import game_framework
import game_world


class can_bullet:
    image = None

    def __init__(self, x=800, y=300, velocity=1):
        if self.image == None:
            self.image = load_image('resources/weapon/cannon_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.power = 70

    def draw(self):
        self.image.draw(self.x + 55, self.y+5, 20, 20)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1270:
            game_world.remove_objects(self)
