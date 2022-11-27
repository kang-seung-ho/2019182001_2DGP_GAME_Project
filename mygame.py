import game_framework
import pico2d

import play_state
import logo_state
import second_play_state
import third_play_state

pico2d.open_canvas(1280, 720)
game_framework.run(logo_state)
pico2d.close_canvas()