from pico2d import *
import game_framework
from boy import Boy
from ui import UI_class
import game_world
from ui import background
from goblin1 import goblin
from fortress import Fortress
import help_state
import title_state
from bullet import bullets

boy = None



def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
            game_framework.push_state(help_state)
        else:
            boy.handle_event(event)

goblin_crowd = None
# 초기화
def enter():
    global boy, goblin_crowd
    boy = Boy()
    ui = UI_class()
    background_UI = background()
    # goblin_1 = goblin()
    fortress1 = Fortress(300, 530)
    fortress2 = Fortress(400, 190)
    goblin_crowd = [goblin() for i in range(21)]

    game_world.add_object(background_UI, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(ui, 0)
    # game_world.add_object(goblin_1, 1)
    game_world.add_object(fortress1, 1)
    game_world.add_object(fortress2, 1)
    for i in range(21):
        game_world.add_object(goblin_crowd[i], 1)

    # game_world.add_collision_pairs(a, b, group)

    game_world.add_collision_pairs(boy.my_bullet, goblin_crowd, 'my_bullet:goblin_crowd')
    game_world.add_collision_pairs(boy, goblin_crowd, 'boy:goblin_crowd')

# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()


    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)

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

def collide(a, b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True




def test_self():
    import play_state

    pico2d.open_canvas(1280, 720)
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
