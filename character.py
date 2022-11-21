from pico2d import *
import game_framework
import game_world
from bullet import Bullet
# import title_state
from cannon import Cannon
from ui import UI_class
import game_over_state

#이벤트 정의
RD, LD, RU, LU, ATTK, UD, DD, UU, DU, ATTKU, CAND, CANU, HEALD, HEALU, POWD, POWU = range(16)
event_name = ['RD', 'LD', 'RU', 'LU', 'ATTK', 'UD', 'DD', 'UU', 'DU', 'ATTKU', 'CAND', 'CANU', 'HEALD', 'HEALU', 'POWD', 'POWU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD, 
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_v): ATTK,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYUP, SDLK_v): ATTKU,
    (SDL_KEYDOWN, SDLK_c): CAND,
    (SDL_KEYUP, SDLK_c): CANU,
    (SDL_KEYDOWN, SDLK_x): HEALD,
    (SDL_KEYUP, SDLK_x): HEALU,
    (SDL_KEYDOWN, SDLK_z): POWD,
    (SDL_KEYUP, SDLK_z): POWU
}

class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        self.diry = 0


    def exit(self, event):
        print('EXIT IDLE')
        if event == ATTK:
            self.fire()
            Bullet.draw(self)
        elif event == CAND:
            self.install_cannon()
            Cannon.draw(self)
        elif event == HEALD:
            self.heal()
        elif event == POWD:
            self.power_up()
        

    def do(self): #상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 5
        if self.hp <= 0:
            game_framework.change_state(game_over)

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 59, 56 * 4, 59, 56, self.x, self.y, 120, 120)
        else:
            self.image.clip_draw(self.frame * 59, 56 * 4, 59, 56, self.x, self.y, 120, 120)




class RUN:
    def enter(self, event): 
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        elif event == UD:
            self.diry += 1
        elif event == UU:
            self.diry -= 1
        elif event == DD:
            self.diry -= 1
        elif event == DU:
            self.diry += 1


    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir #달리고 있다가 나가게 되더라도 현재 방향을 유지하고 나갈 수 있다.
        if event == ATTK:
            self.fire()
            Bullet.draw(self)
        elif event == CAND:
            self.install_cannon()
            Cannon.draw(self)
        elif event == HEALD:
            self.heal()
        elif event == POWD:
            self.power_up()

    def do(self):
        self.frame = (self.frame + 1) % 5
        # x 좌표 변경, 달리기
        self.x += self.dir
        self.y += self.diry

        # self.x += self.dir * 5
        # self.y += self.diry * 5

        if self.x > 1220:
            self.x = self.x - self.dir * 5
        elif self.y > 650:
            self.y = self.y - self.diry * 5
        elif self.x < 50:
            self.x = self.x - self.dir * 5
        elif self.y < 153:
            self.y = self.y - self.diry * 5

        if self.hp <= 0:
            game_framework.change_state(game_over)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 59, 56 * 3, 59, 56, self.x, self.y+8, 120, 120)
            
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 59, 56 * 2, 59, 56, self.x, self.y+8, 120, 120)



class ATTACK:

    def enter(self, event):
        print('attack')
        #
        # if event == RD:
        #     self.dir += 1
        # elif event == LD:
        #     self.dir -= 1
        # elif event == RU:
        #     self.dir -= 1
        # elif event == LU:
        #     self.dir += 1
        # elif event == UD:
        #     self.diry += 1
        # elif event == UU:
        #     self.diry -= 1
        # elif event == DD:
        #     self.diry -= 1
        # elif event == DU:
        #     self.diry += 1

    def exit(self, event):
        print('EXIT attack')
        # self.face_dir = self.dir #달리고 있다가 나가게 되더라도 현재 방향을 유지하고 나갈 수 있다.

    def do(self):
        self.frame = (self.frame + 1) % 5
        if self.hp <= 0:
            game_framework.change_state(game_over)

        # self.x += self.dir
        # self.y += self.diry

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 59, 56 * 0, 59, 56, self.x, self.y+23, 120, 120)
        else:
            self.image.clip_draw(self.frame * 59, 56 * 1, 59, 56, self.x, self.y+23, 120, 120)



#상태변환 기술
next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, ATTK: ATTACK, UD: RUN, UU: RUN, DD: RUN, DU: RUN, ATTKU: RUN, CAND: RUN,
           CANU: RUN, HEALD: RUN, HEALU: RUN, POWD: RUN, POWU: RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, ATTK: ATTACK, UD: IDLE, UU: IDLE, DD: IDLE, DU: IDLE, ATTKU: IDLE,
          CAND: IDLE, CANU: IDLE, HEALD: IDLE, HEALU: IDLE, POWD: IDLE, POWU: IDLE},
    ATTACK: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, ATTK: ATTACK, ATTKU: IDLE, UD: RUN, UU: RUN, DD: RUN, DU: RUN,
             CAND: RUN, CANU: RUN, HEALD: RUN, HEALU: RUN, POWD: RUN, POWU: RUN}
}



class Character:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    
    def __init__(self):
        self.x, self.y = 1280//2, 720//2
        self.frame = 0
        self.dir = 0
        self.face_dir = 1
        self.diry = 0
        self.image = load_image('resources/sprite_sheet/character.png')

        self.q = [] #이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) #초기상태의 entry 액션 수행
        self.hp = 600
        self.cannon_cnt = 0
        self.hp_UI = load_image('resources/ui/hp.png')
        self.fire_sound = load_music('resources/sound/effect/fire_sound.mp3')
        self.fire_sound.set_volume(70)
        self.heal_sound = load_music('resources/sound/effect/heal.mp3')
        self.heal_sound.set_volume(60)
        self.coin = 50
        self.power = 60
        self.power_up_sound = load_music('resources/sound/effect/power_up.mp3')
        self.power_up_sound.set_volume(60)
        # self.cannon_install_sound = load_music()
        # self.cannon_install_sound.set_volume(60)
        self.coin = 50 #적 처치시 코인 획득, 초기 코인 50

        self.font = load_font('resources/system/game_font.ttf', 60)

        self.game_over_sound = load_music('resources/sound/system/game_over.mp3')
        self.game_over_sound.set_volume(80)

    def update(self):
        self.cur_state.do(self) #현재 상태의 do액션 수행

        #이벤트를 확인해서 , 이벤트가 발생했으면,
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self, event) #현재 상태를 나가야 되고.
            try:
                self.cur_state = next_state[self.cur_state][event] #다음 상태를 구한다.
            except KeyError:
                print(self.cur_state, event_name[event])
            self.cur_state.enter(self, event) #다음 상태의 entry action 수행



    def draw(self):
        self.cur_state.draw(self)
        if self.hp > 600:
            self.hp_UI.draw(250, 50, 50, 50)
            self.hp_UI.draw(400, 50, 50, 50)
            self.hp_UI.draw(350, 50, 50, 50)
            self.hp_UI.draw(300, 50, 50, 50)
        if self.hp > 400:
            self.hp_UI.draw(400, 50, 50, 50)
            self.hp_UI.draw(350, 50, 50, 50)
            self.hp_UI.draw(300, 50, 50, 50)
        elif self.hp> 200:
            self.hp_UI.draw(400, 50, 50, 50)
            self.hp_UI.draw(350, 50, 50, 50)
        elif self.hp >= 0:
            self.hp_UI.draw(400, 50, 50, 50)
        else:
            self.game_over_sound.play()
            game_framework.change_state(game_over_state)

        draw_rectangle(*self.get_bb())
        self.font.draw(1000, 80, f'COIN: {self.coin}', (0, 0, 0))

    my_bullet = None
    def fire(self):
        print('fire')
        if self.face_dir == 0:
            self.face_dir = 1
        global my_bullet
        my_bullet = Bullet(self.x + 15, self.y + 15, self.face_dir)
        game_world.bullet_list.append(my_bullet)

        self.fire_sound.play()
        game_world.add_object(my_bullet, 1)
        game_world.add_collision_pairs(my_bullet, None, 'my_bullet:goblin_crowd')



    def install_cannon(self):
        print('install cannon')
        if self.cannon_cnt >= 3:
            pass
        else:
            self.cannon_cnt += 1
            my_cannon = Cannon(self.x, self.y)
            game_world.add_object(my_cannon, 1)
            game_world.add_collision_pairs(my_cannon, None, 'my_cannon:goblin_crowd')
            # self.cannon_install_sound.play()

    def heal(self):
        print('heal')
        if self.hp > 600:
            pass
        else:
            self.hp += 200
            self.heal_sound.play()

    def power_up(self):
        if self.power >= 100:
            pass
        else:
            self.power += 20
            self.power_up_sound.play()


    #59 * 56
    def get_bb(self):
        return self.x-35, self.y-29, self.x+20, self.y+55


    def handle_collision(self, other, group):
        if group == 'boy:goblin_crowd':
            self.hp -= 2




