from pico2d import *
import random
import game_framework
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
object_tree_spring = load_image('tree2.png')
fortress = load_image('fortress.png')
powerup_item = load_image('power_up_arrow.png')
itembox = load_image('itembox.png')
potion = load_image('potion.png')
cannon = load_image('cannon.png')
running = True
background_summer = load_image('map2_summer.png')
frame = 0

x=0
y=0
dirx = 0
diry = 0
while running:
    clear_canvas()
    
    background_summer.draw(WIDTH//2, HEIGHT//2)
    object_tree_spring.draw(400, 650, 120, 120)
    fortress.draw(700, 500, 120, 120)
    object_tree_spring.draw(400, 300, 120, 120)
    fortress.draw(700,200, 120, 120)
    itembox.draw(600, 60, 300 , 140)
    powerup_item.draw(520, 66, 80, 80)
    potion.draw(600, 60, 80, 80)
    cannon.draw(680, 60, 80, 80)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dirx * 5
    y += diry * 5
    if dirx == 0:
        
                
            # character.clip_draw()
        frame = (frame + 1) % 8
        x += dirx * 5
        y += diry * 5
        delay(0.01)


    update_canvas()
    handle_events()







close_canvas()