# objects[0]: 바닥계층
# objects[1]: 상위계층
objects = [[], []]

# 리스트에 추가된 순서대로 그려진다.
# 앞에 그릴지 뒤에 그릴지 처음부터 지정해준다.

collision_group = dict()

bullet_list = []
normal_goblin_cnt = 13
first_boss_cnt = 1
second_state_normal_goblin_cnt = 20
coin = 50
character_power = 40
background_state = 'spring'

def add_object(o, depth):
    objects[depth].append(o)


def remove_objects(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            break

def all_objects():
    for layer in objects:
        for o in layer:
            yield o # 제너레이터가 되어서 모든 객체들을 하나씩 넘겨준다.

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()

def add_collision_pairs(a, b, group):
    if group not in collision_group:
        print('add new group')
        collision_group[group] = [  [] , []  ]

    if a:
        if type(a) == list:
            collision_group[group][0] += a
        else:
            collision_group[group][0].append(a)

    if b:
        if type(b) == list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)

def all_collision_pairs():
    for group, pairs in collision_group.items():
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group


def remove_collision_object(o):
    for pairs in collision_group.values():
        if o in pairs[0]: pairs[0].remove(o)
        elif o in pairs[1]: pairs[1].remove(o)

# def bullet_collision(o):
#     add_collision_pairs(bullet_list, :)