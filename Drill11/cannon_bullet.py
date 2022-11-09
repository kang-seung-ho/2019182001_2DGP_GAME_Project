from pico2d import *
import game_framework
import game_world
from bullet import bullets
import title_state

class can_bullet:
    image = None

    def __init__(self, x=800, y=300, velocity=1):
        if bullets.image == None:
            bullets.image = load_image('cannon.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x + 5, self.y, 20, 20)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1270:
            game_world.remove_objects(self)
