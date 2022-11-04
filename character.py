from pico2d import *
import game_framework
import title_state
import stage_1

RD, LD, RU, LU, UD, UU, DU, DD, ATTK_D = range(9)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU
}

class IDLE:
    def enter(self, event):
        self.attack_state = 1
        self.dirx = 0
        self.diry = 0
    def exit(self):
        pass
        # del character
    def do(self): #상태에 있을 때 지속적으로 행하는 행위
        self.frame = (self.frame + 1) % 5

    def draw(self):
        if self.character_state == 0:
            self.character.clip_draw(self.frame * 59, 56 * 4, 59, 56, self.x, self.y, 120, 120)
        elif self.character_state == 1:
            self.character.clip_draw(self.frame * 59, 56 * 4, 59, 56, self.x, self.y, 120, 120)


class RUN:
    def enter(self, event):
        if event == RD:
            self.dirx += 1
        elif event == LD:
            self.dirx -= 1
        elif event == RU:
            self.dirx -= 1
        elif event == LU:
            self.dirx += 1
        elif event == UD:
            self.diry += 1
        elif event == UU:
            self.diry -= 1
        elif event == DD:
            self.diry -= 1
        elif event == DU:
            self.diry += 1

    def exit(self):
        self.character_state
        #self.face_dir = self.dir #달리고 있다가 나가게 되더라도 현재 방향을 유지하고 나갈 수 있다.
        pass

    def do(self):
        self.frame = (self.frame + 1) % 5
        # self.x = clamp(0, self.x, 700)


        self.x += self.dirx * 5
        self.y += self.diry * 5

        if self.x > 1220:
            self.x = self.x - self.dirx * 5
        elif self.y > 650:
            self.y = self.y - self.diry * 5
        elif self.x < 50:
            self.x = self.x - self.dirx * 5
        elif self.y < 153:
            self.y = self.y - self.diry * 5

        if self.hp <= 0:
            game_framework.change_state(title_state)
        pass

    def draw(self):
        if self.dirx > 0:
            self.character.clip_draw(self.frame * 59, 56 * 2, 59, 56, self.x, self.y, 120, 120)
            self.character_state = 1
        elif self.dirx < 0:
            self.character.clip_draw(self.frame * 59, 56 * 3, 59, 56, self.x, self.y, 120, 120)
            self.character_state = 0


class ATTACK:
    def enter(self, event):
        self.attack_state = 1

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame +1 ) % 8

    def draw(self):
        if self.character_state == 0:
            self.character.clip_draw(self.frame * 59, 56 * 1, 59, 56, self.x, self.y, 120, 120)
        elif self.character_state == 1:
            self.character.clip_draw(self.frame * 59, 56 * 0, 59, 56, self.x, self.y, 120, 120)

next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UU: RUN, UD: RUN, DD: RUN, DU: RUN, ATTK_D: ATTACK },
    RUN: {RU: IDLE, LU: IDLE, RD: RUN, LD: RUN, UU: RUN, UD: RUN, DD: RUN, DU: RUN, ATTK_D: ATTACK },
    ATTACK: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, UU: RUN, UD: RUN, DD: RUN, DU: RUN}
}





class character_class:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def __init__(self):
        self.x, self.y = 1280//2, 720//2
        self.frame = 0
        self.dirx = 0
        self.diry = 0
        self.character_state = 0
        self.character = load_image('character.png')
        self.hp_UI = load_image('hp.png')
        self.hp = 3



        self.q = []  # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None)  # 초기상태의 entry 액션 수행

    def update(self):
        self.cur_state.do(self)  # 현재 상태의 do액션 수행

        # 이벤트를 확인해서 , 이벤트가 발생했다면.
        if self.q:
            event = self.q.pop()
            self.cur_state.exit(self)  # 현재 상태를 나가야 되고.
            self.cur_state = next_state[self.cur_state][event]  # 다음 상태를 구한다.
            self.cur_state.enter(self, event)  # 다음 상태의 entry action 수행

    def draw(self):
        self.cur_state.draw(self)
        delay(0.07)