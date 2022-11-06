from pico2d import *

#이벤트 정의
RD, LD, RU, LU, AD, AU, UD, DD, UU, DU = range(10)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD, 
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_v): AD,
    (SDL_KEYUP, SDLK_v): AU,
    (SDL_KEYDOWN, SDLK_DOWN): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_UP): DU
}

class IDLE:
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0


    def exit(self): 
        print('EXIT IDLE')
        

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


    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir #달리고 있다가 나가게 되더라도 현재 방향을 유지하고 나갈 수 있다.


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

        if self.hp <= 0:
            game_framework.change_state(title_state)

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 59, 56 * 3, 59, 56, self.x, self.y, 120, 120)
            
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 59, 56 * 2, 59, 56, self.x, self.y, 120, 120)



class ATTACK:

    def enter(self, event):
        print('attack')

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

    def exit(self):
        print('EXIT attack')
        self.face_dir = self.dir #달리고 있다가 나가게 되더라도 현재 방향을 유지하고 나갈 수 있다.

    def do(self):
        self.frame = (self.frame + 1) % 5

        self.x += self.dir
        self.y += self.diry

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 59, 56 * 0, 59, 56, self.x, self.y, 120, 120)            
        else:
            self.image.clip_draw(self.frame * 59, 56 * 1, 59, 56, self.x, self.y, 120, 120)



#상태변환 기술
next_state = {
    IDLE: {RU: IDLE, LU: IDLE, RD: RUN, LD: RUN, AD: ATTACK, AU: IDLE, UD: RUN, UU: IDLE, DD: RUN, DU: IDLE},
    RUN: {RU: IDLE, LU: IDLE, RD:RUN, LD: RUN, AD: ATTACK, AU: IDLE, UD: RUN, UU: IDLE, DD: RUN, DU: IDLE},
    ATTACK: {RU: IDLE, LU: IDLE, RD: RUN, LD: RUN, AD: ATTACK, AU: IDLE, UD: RUN, UU: IDLE, DD: RUN, DU: IDLE}
}




class Boy:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 0
        self.face_dir = 1
        self.diry = 0
        self.image = load_image('character.png')

        self.q = [] #이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) #초기상태의 entry 액션 수행
        self.hp = 3

    def update(self):
        self.cur_state.do(self) #현재 상태의 do액션 수행

        #이벤트를 확인해서 , 이벤트가 발생했으면,
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self) #현재 상태를 나가야 되고.
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 구한다.
            self.cur_state.enter(self, event) #다음 상태의 entry action 수행
        

    def draw(self):
        self.cur_state.draw(self)