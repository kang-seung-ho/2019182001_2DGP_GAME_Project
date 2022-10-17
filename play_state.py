from pico2d import *
import random
import game_framework
# import logo_state


WIDTH, HEIGHT = 1280, 720

def handle_events():
    global running
    global dirx
    global diry
    global character_state
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_v:
                character_state = 2

            if event.key == SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
            elif event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1
            elif event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1



open_canvas(WIDTH, HEIGHT)

dirx, diry = 0,0
x = WIDTH//2
y = HEIGHT//2
background_spring = load_image('map1_spring_temp.png')
running = True
stage = 1

frame=0
character_state = 0

class monsters:
    def __init__(self):
        rand_y = randint(0, 3+1)
        monster_y = 0
        if rand_y == 0:
            monster_y = 650
        elif rand_y == 1:
            monster_y == 530
        elif rand_y ==2:
            monster_y == 410
        elif rand_y == 3:
            monster_y == 290

        self.x, self.y = 1200, monster_y
        self.frame = 0
        self.image = load_image('goblinsword.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*64, 64*2, 64, 64, self.x, self.y, 120, 120)




round1_monster = [monsters for i in range (20)] #라운드 1에서 몬스터 20마리 출현

# game_framework.run(logo_state)

object_tree_spring = load_image('tree2.png')
fortress = load_image('fortress.png')
powerup_item = load_image('power_up_arrow.png')
itembox = load_image('itembox.png')
potion = load_image('potion.png')
cannon = load_image('cannon.png')
attack = load_image('gun.png')
hp = load_image('hp.png')
character = load_image('character.png')
character_hp = 3

while running:
    clear_canvas()
    
    background_spring.draw(WIDTH//2, HEIGHT//2)
    object_tree_spring.draw(400, 650, 120, 120)
    fortress.draw(700, 530, 120, 120)
    object_tree_spring.draw(400, 300, 120, 120)
    fortress.draw(700, 190, 120, 120)
    itembox.draw(600, 60, 300 , 140)
    powerup_item.draw(520, 66, 80, 80)
    potion.draw(600, 60, 80, 80)
    cannon.draw(680, 60, 80, 80)
    attack.draw(800, 60, 80, 80)
    if character_hp == 3:
        hp.draw(400, 50, 50, 50)
        hp.draw(350, 50, 50, 50)
        hp.draw(300, 50, 50, 50)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 5
    x += dirx * 5
    y += diry * 5

    if dirx == 0:
        if character_state == 0:
            character.clip_draw(frame * 59, 56*4 , 59, 56, x, y, 120, 120)
        elif character_state == 1:
            character.clip_draw(frame * 59, 56*4 , 59, 56, x, y, 120, 120)
    if dirx > 0 :
        character.clip_draw(frame * 59, 56*2 , 59, 56, x, y, 120, 120)
        character_state = 1
    elif dirx < 0:
        character.clip_draw(frame * 59, 56*3 , 59, 56, x, y, 120, 120)
        character_state = 0

    if x > 1220:
        x = x - dirx*7
    elif y > 650:
        y = y - diry*7
    elif x < 50:
        x = x - dirx*7
    elif y < 153:
        y = y - diry*7

    update_canvas()
                
    
    delay(0.07)   


    handle_events()







close_canvas()