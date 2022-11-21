import game_framework
import pico2d

import play_state
import logo_state

pico2d.open_canvas(1280, 720)
game_framework.run(logo_state)
pico2d.close_canvas()