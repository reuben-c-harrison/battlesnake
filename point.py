class Point:

    def __init__(self,
                 components,
                 x,
                 y,
                 safe=['F', '.', 'T', 't'],
                 rank=0,
                 direction="none",
                 parent=None,
                 g_score=0,
                 h_score=0):
        self.components = components
        self.board = components.board
        self.x = x
        self.y = y
        self.width = components.width
        self.height = components.height
        self.rank = rank
        self.direction = direction
        self.parent = parent
        self.safe = safe
        self.g_score = g_score
        self.h_score = h_score
        self.f_score = g_score + h_score

    def get_symbol(self):
        return self.board[self.y][self.x]

    def check_safe(self):
        return self.get_symbol() in self.safe

    def get_neighbours(self, target_x=None, target_y=None):
        neighbours = []
        new_g_score = self.g_score + 1

        if self.y > 0:
            h = abs(self.x - target_x) + abs((self.y - 1) - target_y) if target_x is not None else 0
            down = Point(self.components, self.x, self.y - 1, self.safe,
                         self.rank + 1, "down", self, new_g_score, h)
            if down.check_safe():
                neighbours.append(down)
        if self.y < (self.height - 1):
            h = abs(self.x - target_x) + abs((self.y + 1) - target_y) if target_x is not None else 0
            up = Point(self.components, self.x, self.y + 1, self.safe,
                       self.rank + 1, "up", self, new_g_score, h)
            if up.check_safe():
                neighbours.append(up)
        if self.x < (self.width - 1):
            h = abs((self.x + 1) - target_x) + abs(self.y - target_y) if target_x is not None else 0
            right = Point(self.components, self.x + 1, self.y, self.safe,
                          self.rank + 1, "right", self, new_g_score, h)
            if right.check_safe():
                neighbours.append(right)
        if self.x > 0:
            h = abs((self.x - 1) - target_x) + abs(self.y - target_y) if target_x is not None else 0
            left = Point(self.components, self.x - 1, self.y, self.safe,
                         self.rank + 1, "left", self, new_g_score, h)
            if left.check_safe():
                neighbours.append(left)
        return neighbours

    def get_move(self, prev_move="none"):
        if self.direction == "none":
            return prev_move
        elif self.parent is None:
            return self.direction
        else:
            return self.parent.get_move(self.direction)

    def __eq__(self, other):
        if isinstance(other, Point):
            equal = (self.x == other.x) and (self.y == other.y)
            return equal
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Point):
            return self.f_score < other.f_score
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y))
