from pico2d import *
import game_framework
# import title_state

image = None
sound = None
def enter(): #객체 생성하는 함수
    global image, sound
    image = load_image('game_over_img.png')
    sound = load_music('game_over.mp3')
    sound.set_volume(70)

def exit():
    global image
    del image

def update():
    pass

def draw():
    global sound
    clear_canvas()
    image.draw(1280//2, 720//2)
    sound.play()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.change_state(title_state)



