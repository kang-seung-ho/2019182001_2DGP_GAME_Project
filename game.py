from pico2d import *
import random
import game_framework
# import logo_state


WIDTH, HEIGHT = 1280, 720

def handle_events():
    global running
    global dirx
    global diry
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
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
background_spring = load_image('map1_spring.png')
running = True
stage = 1

frame=0
character_state = 0

class monsters:
    def __init__(self):
        self.x, self.y = 1200, random.randint(20, 600)
        self.frame = random.randint(0, 7)
        self.image = load_image('goblinsword.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 3

    def draw(self):
        self.image.clip_draw(self.frame*64, 64*2, 64, 64, self.x, self.y, 144, 144)

def character_draw(location, x, y):
    character.clip_draw()


round1_monster = [monsters for i in range (20)] #라운드 1에서 몬스터 20마리 출현

# game_framework.run(logo_state)

object_tree_spring = load_image('tree2.png')
fortress = load_image('fortress.png')
powerup_item = load_image('power_up_arrow.png')
itembox = load_image('itembox.png')
potion = load_image('potion.png')
cannon = load_image('cannon.png')
while running:
    clear_canvas()
    
    background_spring.draw(WIDTH//2, HEIGHT//2)
    object_tree_spring.draw(400, 650, 120, 120)
    fortress.draw(700, 500, 120, 120)
    object_tree_spring.draw(400, 300, 120, 120)
    fortress.draw(700,200, 120, 120)
    itembox.draw(600, 60, 300 , 140)
    powerup_item.draw(520, 67, 80, 80)
    potion.draw(600, 60, 80, 80)
    cannon.draw(680, 60, 80, 80)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    y += diry * 5
    if dirx == 0:
        if character_state == 0:
            pass
            # character.clip_draw(frame*, )
        elif character_state == 1:
            pass
                
            # character.clip_draw()
        frame = (frame + 1) % 8
        x += dirx * 5
        y += diry * 5
        delay(0.01)


    update_canvas()
    handle_events()







close_canvas()