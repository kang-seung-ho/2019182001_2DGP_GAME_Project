from pico2d import *
import game_framework
from character import Character
from ui import UI_class
import game_world
from ui import background
from normal_goblin import Normal_goblin
from fortress import Fortress
import help_state
import title_state
import third_game_clear_state
from tree import Tree
from boss_monster import Boss_monster
from special_goblin import Special_goblin

boy = None
bossmonster_condition = 0
special_monster_condition = 0

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
fortress1 = None
fortress2 = None
fortress3 = None
tree1 = None
tree2 = None
tree3 = None
# 초기화
def enter():
    game_world.collision_group.clear()
    game_world.background_state = 'winter'
    global boy, goblin_crowd, font
    global fortress1, fortress2, fortress3
    global tree1, tree2, tree3
    boy = Character()
    ui = UI_class()
    background_UI = background()
    fortress1 = Fortress(300, 530)
    fortress2 = Fortress(400, 190)
    fortress3 = Fortress(600, 190)
    goblin_crowd = [Normal_goblin() for i in range(30)]
    tree1 = Tree(700, 295)
    tree2 = Tree(400, 655)
    tree3 = Tree(800, 420)


    game_world.add_object(background_UI, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(ui, 0)
    game_world.add_object(fortress1, 1)
    game_world.add_object(fortress2, 1)
    game_world.add_object(fortress3, 1)
    game_world.add_object(tree1, 1)
    game_world.add_object(tree2, 1)
    game_world.add_object(tree3, 1)
    for i in range(30):
        game_world.add_object(goblin_crowd[i], 1)

    game_world.add_collision_pairs(boy, goblin_crowd, 'boy:goblin_crowd')
    game_world.add_collision_pairs(fortress1, goblin_crowd, 'fortress1:goblin_crowd')
    game_world.add_collision_pairs(fortress2, goblin_crowd, 'fortress2:goblin_crowd')
    game_world.add_collision_pairs(fortress3, goblin_crowd, 'fortress2:goblin_crowd')
    game_world.add_collision_pairs(tree1, goblin_crowd, 'tree1:goblin_crowd')
    game_world.add_collision_pairs(tree2, goblin_crowd, 'tree2:goblin_crowd')
    game_world.add_collision_pairs(tree3, goblin_crowd, 'tree2:goblin_crowd')
    game_world.add_collision_pairs(None, goblin_crowd, 'my_bullet:goblin_crowd')
    game_world.add_collision_pairs(None, goblin_crowd, 'my_cannon:goblin_crowd')
    game_world.add_collision_pairs(None, goblin_crowd, 'cannon_bullet:goblin_crowd')
    # print('third play state')

# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()


    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            # print('COLLISION ', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)
    global  bossmonster_condition, special_monster_condition
    if game_world.third_state_normal_goblin_cnt == 10 and bossmonster_condition == 0: #보스몬스터 출현
        bossmonster_condition = 1
        bosses = [Boss_monster() for i in range(3)]

        for i in range(3):
            game_world.add_object(bosses[i], 1)

        game_world.add_collision_pairs(None, bosses, 'my_bullet:boss')
        game_world.add_collision_pairs(boy, bosses, 'boy:boss')
        game_world.add_collision_pairs(fortress1, bosses, 'fortress1:boss')
        game_world.add_collision_pairs(fortress2, bosses, 'fortress2:boss')
        game_world.add_collision_pairs(fortress3, bosses, 'fortress3:boss')
        game_world.add_collision_pairs(tree1, bosses, 'tree1:boss')
        game_world.add_collision_pairs(tree2, bosses, 'tree2:boss')
        game_world.add_collision_pairs(tree3, bosses, 'tree2:boss')
        game_world.add_collision_pairs(None, bosses, 'my_bullet:boss')
        game_world.add_collision_pairs(None, bosses, 'my_cannon:boss')
        game_world.add_collision_pairs(None, bosses, 'cannon_bullet:boss')

    if game_world.third_state_normal_goblin_cnt == 15 and special_monster_condition == 0:
        special_monster_condition = 1
        special_goblins = [Special_goblin() for i in range(6)]
        for i in range(6):
            game_world.add_object(special_goblins[i], 1)

        game_world.add_collision_pairs(None, special_goblins, 'my_bullet:special_goblin')
        game_world.add_collision_pairs(boy, special_goblins, 'boy:special_goblin')
        game_world.add_collision_pairs(fortress1, special_goblins, 'fortress1:special_goblin')
        game_world.add_collision_pairs(fortress2, special_goblins, 'fortress2:special_goblin')
        game_world.add_collision_pairs(fortress3, special_goblins, 'fortress3:special_goblin')
        game_world.add_collision_pairs(tree1, special_goblins, 'tree1:special_goblin')
        game_world.add_collision_pairs(tree2, special_goblins, 'tree2:special_goblin')
        game_world.add_collision_pairs(tree3, special_goblins, 'tree3:special_goblin')
        game_world.add_collision_pairs(None, special_goblins, 'my_bullet:special_goblin')
        game_world.add_collision_pairs(None, special_goblins, 'my_cannon:special_goblin')
        game_world.add_collision_pairs(None, special_goblins, 'cannon_bullet:special_goblin')

    if game_world.third_state_normal_goblin_cnt <= 0 and game_world.third_stage_special_goblin_cnt <= 0 and game_world.third_boss_cnt <= 0:
        game_framework.change_state(third_game_clear_state)



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
    import third_play_state

    pico2d.open_canvas(1280, 720)
    game_framework.run(third_play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
