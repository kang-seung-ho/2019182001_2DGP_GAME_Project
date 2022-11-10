from pico2d import *
import game_framework
from boy import Boy
from ui import UI_class
import game_world
from ui import background
from goblin1 import goblin
from fortress import Fortress

boy = None



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
    global boy
    boy = Boy()
    ui = UI_class()
    background_UI = background()
    goblin_1 = goblin()
    fortress1 = Fortress(300, 530)
    fortress2 = Fortress(400, 190)


    game_world.add_object(background_UI, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(ui, 0)
    game_world.add_object(goblin_1, 1)
    game_world.add_object(fortress1, 1)
    game_world.add_object(fortress2, 1)

# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

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
