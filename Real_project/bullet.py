from pico2d import *
import game_world

class bullets:
    image = None

    def __init__(self, x=800, y=300, velocity=1):
        if bullets.image == None:
            bullets.image = load_image('bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        # self.power = 35



    def draw(self):
        self.image.draw(self.x + 5, self.y, 20, 20)
        draw_rectangle(*self.get_bb())


    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1270:
            game_world.remove_objects(self)


    def get_bb(self):
        return self.x-8, self.y-10, self.x+15, self.y+10

    def handle_collision(self, other, group):
        if group == 'my_bullet:goblin_crowd':
            game_world.remove_objects(self)
