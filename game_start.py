import pico2d
import game_framework
import stage_1
import logo_state
pico2d.open_canvas(1280, 720)
game_framework.run(logo_state) #테스트를 위해 로고말고 바로 들어감
pico2d.clear_canvas()

