import collections
from point import Point


def a_star(components, target, safe):
    you_x = components.head['x']
    you_y = components.head['y']
    _open = collections.deque([Point(components, you_x, you_y, safe)])
    closed = set()

    while True:
        try:
            top = _open.popleft()
        except IndexError:
            return []
        if top.get_symbol() == target:
            break
        closed.add(top)
        neighbours = top.get_neighbours()
        for neighbour in neighbours:
            in_open, in_closed = False, False
            for value in tuple(_open):
                if value == neighbour:
                    if value.rank > neighbour.rank:
                        _open.remove(value)
                    else:
                        in_open = True
            for value in tuple(closed):
                if value == neighbour:
                    if value.rank > neighbour.rank:
                        closed.remove(value)
                    else:
                        in_closed = True
            if (not in_open) and (not in_closed):
                _open.append(neighbour)
    return top.get_move()


def get_food(components, safe=['F', '.', 'T', 't']):
    print("GET FOOD")
    return a_star(components, 'F', safe)


def chase_tail(components, safe=['F', '.', 'T']):
    print("CHASE TAIL")
    return a_star(components, 'T', safe)
