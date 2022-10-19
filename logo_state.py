from pico2d import *
import game_framework
import play_state
import title_state
import stage_1

# running = True
image = None
logo_time = 0.0

def enter(): #객체 생성하는 함수
    global image
    image = load_image('tuk_credit.png')

def exit():
    global image
    del image

def update():
    #logo time을 계산하고, 그 결과에 따라 1초가 넘으면 running = False
    global logo_time, running
    delay(0.01)
    logo_time += 0.01

    if logo_time >= 0.5:
        logo_time = 0
        game_framework.change_state(title_state)

def draw():
    clear_canvas()
    image.draw(640,360)
    update_canvas()

def handle_events():
    events = get_events()





