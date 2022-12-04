from pico2d import *
import game_world

class UI_class:
    def __init__(self):
        self.powerup_item = load_image('resources/ui/power_up_arrow.png')
        self.itembox = load_image('resources/ui/itembox.png')
        self.potion = load_image('resources/ui/potion.png')
        self.attack = load_image('resources/ui/gun.png')
        self.cannon = load_image('resources/ui/cannon.png')
        self.bgm = load_music('resources/sound/bgm/stage1_main_bgm.mp3')
        self.bgm.set_volume(100)
        self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.itembox.draw(600, 60, 300, 140)
        self.powerup_item.draw(520, 66, 80, 80)
        self.potion.draw(600, 60, 80, 80)
        self.attack.draw(800, 60, 80, 80)
        self.cannon.draw(680, 60, 80, 80)


class background:
    def __init__(self):
        if game_world.background_state == 'spring':
            self.background = load_image('resources/map/map1_spring.png')
        elif game_world.background_state == 'summer':
            self.background = load_image('resources/map/map2_summer.png')
        elif game_world.background_state == 'winter':
            self.background = load_image('resources/map/map3_winter.png')

    def update(self):
        pass

    def draw(self):
        self.background.draw(1280 // 2, 720 // 2)