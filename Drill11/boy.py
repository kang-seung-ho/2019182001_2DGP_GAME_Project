from pico2d import *
import game_framework
import game_world
from bullet import bullets
# import title_state
from cannon import Cannon

#이벤트 정의
RD, LD, RU, LU, ATTK, UD, DD, UU, DU, ATTKU, CAND, CANU = range(12)
event_name = ['RD', 'LD', 'RU', 'LU', 'ATTK', 'UD', 'DD', 'UU', 'DU', 'ATTKU', 'CAND', 'CANU']

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
    (SDL_KEYUP, SDLK_c): CANU
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
            bullets.draw(self)
        elif event == CAND:
            self.install_cannon()
            Cannon.draw(self)
        

    def do(self): #상태에 있을 때 지속적으로 행하는 행위, 숨쉬기
        self.frame = (self.frame + 1) % 5

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
            bullets.draw(self)
        elif event == CAND:
            self.install_cannon()
            Cannon.draw(self)

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
            self.x = self.x + self.dir * 5
        elif self.y < 153:
            self.y = self.y + self.diry * 5

        # if self.hp <= 0:
        #     game_framework.change_state(title_state)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 59, 56 * 3, 59, 56, self.x, self.y, 120, 120)
            
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 59, 56 * 2, 59, 56, self.x, self.y, 120, 120)



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

        # self.x += self.dir
        # self.y += self.diry

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 59, 56 * 0, 59, 56, self.x, self.y, 120, 120)            
        else:
            self.image.clip_draw(self.frame * 59, 56 * 1, 59, 56, self.x, self.y, 120, 120)



#상태변환 기술
next_state = {
    IDLE:   {RU: RUN, LU: RUN, RD: RUN, LD: RUN, ATTK: ATTACK, UD: RUN, UU: RUN, DD: RUN, DU: RUN, ATTKU: RUN, CAND: RUN, CANU: RUN},
    RUN:    {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, ATTK: ATTACK, UD: IDLE, UU: IDLE, DD: IDLE, DU: IDLE, ATTKU: IDLE, CAND: IDLE, CANU: IDLE},
    ATTACK: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, ATTK: ATTACK, ATTKU: IDLE, UD: RUN, UU: RUN, DD: RUN, DU: RUN, CAND: RUN, CANU: RUN}
}




class Boy:

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
        self.image = load_image('character.png')

        self.q = [] #이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) #초기상태의 entry 액션 수행
        self.hp = 500
        self.cannon_cnt = 0

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

    def fire(self):
        print('fire')
        if self.face_dir == 0:
            self.face_dir = 1
        my_bullet = bullets(self.x, self.y, self.face_dir)
        game_world.add_object(my_bullet, 1)

    def install_cannon(self):
        print('install cannon')
        if self.cannon_cnt >= 3:
            pass
        else:
            self.cannon_cnt += 1
            my_cannon = Cannon(self.x, self.y)
            game_world.add_object(my_cannon, 1)

