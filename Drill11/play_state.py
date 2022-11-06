from pico2d import *
import game_framework
from grass import Grass
from boy import Boy
from ui import UI_class

boy = None
grass = None
ui = None



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass, ui
    boy = Boy()
    grass = Grass()
    ui = UI_class()

# 종료
def exit():
    global boy, grass
    del boy
    del grass
    del ui

def update():
    boy.update()

def draw_world():
    grass.draw()
    boy.draw()
    ui.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass




def test_self():
    import play_state

    pico2d.open_canvas(1280, 720)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
