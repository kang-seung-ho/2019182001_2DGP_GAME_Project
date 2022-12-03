import game_world
from pico2d import *
import game_framework
import third_play_state

image = None
sound = None
def enter(): #객체 생성하는 함수
    global image, sound
    image = load_image('resources/system/game_clear.png')
    sound = load_wav('resources/sound/system/stage_clear.wav')
    sound.set_volume(70)
    sound.play()
    game_world.cannon_cnt = 0

def exit():
    global image
    del image

def update():
    pass

def draw():
    global sound
    clear_canvas()
    image.draw(1280//2, 720//2)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_SPACE:
                    game_framework.change_state(third_play_state)



