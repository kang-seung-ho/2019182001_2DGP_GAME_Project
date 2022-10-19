from pico2d import *
import random
import game_framework
import logo_state
import title_state

WIDTH, HEIGHT = 1280, 720

def handle_events():
    global running
    global dirx
    global diry
    global character_state
    global attack_state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_v: #공격모션
                attack_state = 1
            elif event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_v:
                attack_state = 0
            elif event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1



# open_canvas(WIDTH, HEIGHT)

dirx, diry = 0,0
x = WIDTH//2
y = HEIGHT//2

running = True
stage = 1

frame=0
character_state = 0
attack_state = 0

class character_class:
    def __init__(self):
        
        self.x, self.y = WIDTH//2, HEIGHT//2
        self.frame = 0
        self.character = load_image('character.png')
        self.hp = 3
        self.direction = 1
        self.character_state = 0
        self.hp_UI = load_image('hp.png')

    def update(self):
        global dirx, diry
        self.frame = (self.frame + 1) % 5
        self.x += dirx * 5
        self.y += diry * 5

        if self.x > 1220:
            self.x = self.x - dirx*7
        elif self.y > 650:
            self.y = self.y - diry*7
        elif self.x < 50:
            self.x = self.x - dirx*7
        elif self.y < 153:
            self.y = self.y - diry*7

    def draw(self):
        if attack_state == 1: #공격키가 눌린 경우.
            if self.character_state == 0:
                self.character.clip_draw(self.frame* 59, 56*1, 59, 56, self.x, self.y, 120, 120)
            elif self.character_state == 1:
                self.character.clip_draw(self.frame* 59, 56*0, 59, 56, self.x, self.y, 120, 120)
        elif dirx == 0:
            if self.character_state == 0:
                self.character.clip_draw(self.frame * 59, 56*4 , 59, 56, self.x, self.y, 120, 120)
            elif self.character_state == 1:
                self.character.clip_draw(self.frame * 59, 56*4 , 59, 56, self.x, self.y, 120, 120)
        elif dirx > 0 :
            self.character.clip_draw(self.frame * 59, 56*2 , 59, 56, self.x, self.y, 120, 120)
            self.character_state = 1
        elif dirx < 0:
            self.character.clip_draw(self.frame * 59, 56*3 , 59, 56, self.x, self.y, 120, 120)
            self.character_state = 0

        if character.hp == 3:
            self.hp.draw(400, 50, 50, 50)
            self.hp.draw(350, 50, 50, 50)
            self.hp.draw(300, 50, 50, 50)
        elif character.hp == 2:
            self.hp.draw(400, 50, 50, 50)
            self.hp.draw(350, 50, 50, 50)
        elif character.hp == 1:
            self.hp.draw(400, 50, 50, 50)
        else:
            pass #타이틀 화면으로 가는 프레임워크 코드 넣기




        


class monsters:
    def __init__(self):
        rand_x = random.randint(1300, 1700)
        rand_y = random.randint(0, 4+1)
        monster_y = 190
        if rand_y == 0:
            monster_y = 650
        elif rand_y == 1:
            monster_y = 530
        elif rand_y ==2:
            monster_y = 410
        elif rand_y == 3:
            monster_y = 300
        elif rand_y == 4:
            monster_y = 190

        self.hp = 300

        self.x, self.y = rand_x, monster_y
        self.frame = 0
        self.image = load_image('goblinsword.png')

    def update(self):
        self.frame = random.randint(0, 8)
        self.x -= 1

    def draw(self):
        self.image.clip_draw(self.frame*64, 64*1, 64, 64, self.x, self.y, 120, 120)


class tree_object():
    def __init__(self):
        self.hp = 200
        self.object_tree_spring = load_image('tree2.png')

    def draw(self):
        self.object_tree_spring.draw(400, 650, 120, 120)
        self.object_tree_spring.draw(400, 300, 120, 120)

class fortess_object():
    def __init__(self):
        self.hp = 350
        self.fortress = load_image('fortress.png')

    def draw(self):
        self.fortress.draw(700, 530, 120, 120)
        self.fortress.draw(700, 190, 120, 120)

class UI_DRAWING():
    def __init__(self):
        self.background_spring = load_image('map1_spring_temp.png')
        self.powerup_item = load_image('power_up_arrow.png')
        self.itembox = load_image('itembox.png')
        self.potion = load_image('potion.png')
        self.cannon = load_image('cannon.png')
        self.attack = load_image('gun.png')
    def draw(self):
        self.background_spring.draw(WIDTH//2, HEIGHT//2)
        self.itembox.draw(600, 60, 300 , 140)
        self.powerup_item.draw(520, 66, 80, 80)
        self.potion.draw(600, 60, 80, 80)
        self.cannon.draw(680, 60, 80, 80)
        self.attack.draw(800, 60, 80, 80)


round1_monster = None


character = None
# monster1 = None
trees = None
UI = None
fortress = None

def enter():
    global character, monster1, trees
    character = character_class()
    round1_monster = [monsters() for i in range (20)] #라운드 1에서 몬스터 20마리 출현
    trees = tree_object()
    UI = UI_DRAWING()
    fortress = fortess_object()
    running = True

def update():
    character.update()
    round1_monster.update()
    



def exit():
    global character, round1_monster
    del character
    del round1_monster

def draw():
    clear_canvas()
    character.draw()
    round1_monster.draw()
    trees.draw()
    UI.draw()
    fortress.draw()
    update_canvas()


# while running:
#     clear_canvas()    
#     object_draw()   
#     handle_events()
#     character.update()
#     for monsters in round1_monster:
#         monsters.update()

#     character.draw()
    
#     for monsters in round1_monster:
#         monsters.draw()


#     update_canvas()

#     delay(0.07)

#     handle_events()





# close_canvas()