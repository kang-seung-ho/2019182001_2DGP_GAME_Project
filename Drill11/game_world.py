# objects[0]: 바닥계층
# objects[1]: 상위계층
objects = [[], []]

# 리스트에 추가된 순서대로 그려진다.
# 앞에 그릴지 뒤에 그릴지 처음부터 지정해준다.


def add_object(o, depth):
    objects[depth].append(o)


def remove_objects(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
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