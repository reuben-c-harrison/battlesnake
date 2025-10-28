import random
from point import Point
from algo import bfs


def avoid_self_and_borders_randomly(components, safe=['F', '.', 't']):
  point = Point(components, components.head['x'], components.head['y'], safe)
  directions = list()

  for neighbour in point.get_neighbours():
    directions.append(neighbour.direction)

  if len(directions) == 0:
    return directions
  return random.choice(directions)


def hunt(components, safe=['F', '.', 'T', 't', 'h']):
  move = bfs(components, 'h', safe)
  return move


def decide_move(components):
  if len(components.snakes) == 2 and (
      len(components.body) - len(components.snakes[0]['body']) >= 1
      or len(components.body) - len(components.snakes[1]['body']) >= 1):
    move = hunt(components)
  else:
    move = bfs(components, 'F', ['F', '.', 't'])
  if len(move) == 0:
    move = avoid_self_and_borders_randomly(components)
  return move
