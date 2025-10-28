from point import Point
import collections


class Board:

  def __init__(self, components):
    self.components = components
    self.create_board()
    self.add_food()
    self.add_snakes()

  def create_board(self):
    board = []
    for i in range(self.components.height):
      board.append(['.'] * self.components.width)
    self.components.board = board

  def add_food(self):
    for food in self.components.food:
      self.components.board[food['y']][food['x']] = 'F'

  def add_snakes(self):
    board = self.components.board
    for snake in self.components.snakes:
      if snake['id'] == self.components.id:
        for body in self.components.body:
          board[body['y']][body['x']] = 'Y'

        board[self.components.head['y']][self.components.head['x']] = 'H'

        if self.components.turn > 0:
          board[self.components.body[-1]['y']][self.components.body[-1]
                                               ['x']] = 'T'
        continue

      for body in snake['body']:
        board[body['y']][body['x']] = 'o'

        board[snake['body'][0]['y']][snake['body'][0]['x']] = 'h'

        if len(snake['body']) > 3:
          board[snake['body'][-1]['y']][snake['body'][-1]['x']] = 't'
        if len(snake['body']) >= len(self.components.body):
          for neighbour in Point(self.components, snake['body'][0]['x'],
                                 snake['body'][0]['y']).get_neighbours():
            board[neighbour.y][neighbour.x] = '*'

  def print_board(self):
    board = self.components.board

    x_label = 1
    print("  ", end=" ")
    for coord in board[0]:
      if x_label < 10:
        print(x_label, end="  ")
      else:
        print(x_label, end=" ")
      x_label += 1
    print()

    y_label = 1
    for x in board:
      if y_label < 10:
        print(y_label, end="  ")
      else:
        print(y_label, end=" ")

      for coord in x:
        print(coord, end="  ")
      print()
      y_label += 1
