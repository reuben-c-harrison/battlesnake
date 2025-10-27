class Board:

  def __init__(self, components):
    self.components = components
    self.create_board()
    self.add_food()
    self.add_snakes()

  def create_board(self):
    board = []
    for i in range(self.components.height):
      board.append(['O'] * self.components.width)
    self.components.board = board

  def add_food(self):
    for food in self.components.food:
      self.components.board[food['y']][food['x']] = 'F'

  def add_snakes(self):
    for snake in self.components.snakes:
      if snake['id'] == self.components.id:
        for body in snake['body']:
          self.components.board[body['y']][body['x']] = 'Y'
