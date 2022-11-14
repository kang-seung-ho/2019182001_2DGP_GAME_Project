from pico2d import *
import game_framework

image = None
def enter(): #객체 생성하는 함수
    global image
    image = load_image('help_img.png')

def exit():
    global image
    del image

def update():
    pass

def draw():
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
                    game_framework.pop_state()
