import random

from a_star import get_food
from point import Point


def avoid_self_and_borders_randomly(components, safe=['F', '.', 'T', 't']):
  print("AVOID SELF AND BORDERS RANDOMLY")
  you_x = components.head['x']
  you_y = components.head['y']
  point = Point(components, you_x, you_y, safe)
  directions = list()

  for neighbour in point.get_neighbours():
    directions.append(neighbour.direction)

  if len(directions) == 0:
    return directions
  return random.choice(directions)


def decide_move(components):
  move = get_food(components)
  return move
