from pico2d import *

class UI_class:
    def __init__(self):
        self.powerup_item = load_image('power_up_arrow.png')
        self.itembox = load_image('itembox.png')
        self.potion = load_image('potion.png')
        self.cannon = load_image('cannon.png')
        self.attack = load_image('gun.png')


    def update(self):
        pass

    def draw(self):
        self.itembox.draw(600, 60, 300, 140)
        self.powerup_item.draw(520, 66, 80, 80)
        self.potion.draw(600, 60, 80, 80)
        self.cannon.draw(680, 60, 80, 80)
        self.attack.draw(800, 60, 80, 80)


class background:
    def __init__(self):
        self.background = load_image('map1_spring.png')

    def update(self):
        pass

    def draw(self):
        self.background.draw(1280 // 2, 720 // 2)