class Point:

    def __init__(self,
                 components,
                 x,
                 y,
                 safe=['F', '.', 'T', 't'],
                 rank=0,
                 direction="none",
                 parent=None):
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

    def get_symbol(self):
        return self.board[self.y][self.x]

    def check_safe(self):
        return self.get_symbol() in self.safe

    def get_neighbors(self):
        neighbors = []

        if self.y > 0:
            up = Point(self.components, self.x, self.y - 1, self.safe,
                       self.rank + 1, "up", self)
            if up.check_safe():
                neighbors.append(up)
        if self.y < (self.height - 1):
            down = Point(self.components, self.x, self.y + 1, self.safe,
                         self.rank + 1, "down", self)
            if down.check_safe():
                neighbors.append(down)
        if self.x < (self.width - 1):
            right = Point(self.components, self.x + 1, self.y, self.safe,
                          self.rank + 1, "right", self)
            if right.check_safe():
                neighbors.append(right)
        if self.x > 0:
            left = Point(self.components, self.x - 1, self.y, self.safe,
                         self.rank + 1, "left", self)
            if left.check_safe():
                neighbors.append(left)

        return neighbors

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

    def __hash__(self):
        return hash((self.x, self.y))
