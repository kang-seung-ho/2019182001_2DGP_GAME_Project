from pico2d import *
import random
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
background_spring = load_image('')
running = True
stage = 1

character=load_image()
monster1 = load_image('')
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

while running:
    clear_canvas()
    if stage == 1:
        # backgroud_spring.draw(WIDTH//2, HEIGHT//2)
        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        x += dirx * 5
        y += diry * 5

        if dirx == 0:
            if character_state == 0:
                character.clip_draw()

        frame = (frame + 1) % 8
        x += dirx * 5
        y += diry * 5
        delay(0.01)


    update_canvas()
    handle_events()







close_canvas()