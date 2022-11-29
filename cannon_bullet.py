from pico2d import *
import game_framework
import game_world


class Can_bullet:
    image = None

    def __init__(self, x=800, y=300, velocity=1):
        if self.image == None:
            self.image = load_image('resources/weapon/cannon_bullet.png')
        self.x, self.y, self.velocity = x + 55, y + 5, velocity
        self.power = 70

    def draw(self):
        self.image.draw(self.x, self.y, 20, 20)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1270:
            game_world.remove_objects(self)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'cannon_bullet:goblin_crowd':
            game_world.remove_objects(self)
        elif group == 'cannon_bullet:boss':
            game_world.remove_objects(self)
