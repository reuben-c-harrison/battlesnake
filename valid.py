def backward(my_head, my_neck, is_move_safe):
  if my_neck["x"] < my_head["x"]:
    is_move_safe["left"] = False
  elif my_neck["x"] > my_head["x"]:
    is_move_safe["right"] = False
  elif my_neck["y"] < my_head["y"]:
    is_move_safe["down"] = False
  elif my_neck["y"] > my_head["y"]:
    is_move_safe["up"] = False
  return is_move_safe


def out_of_bounds(my_head, board_width, board_height, is_move_safe):
  if my_head["x"] == 0:
    is_move_safe["left"] = False
  elif my_head["x"] == board_width - 1:
    is_move_safe["right"] = False
  elif my_head["y"] == 0:
    is_move_safe["down"] = False
  elif my_head["y"] == board_height - 1:
    is_move_safe["up"] = False
  return is_move_safe


def is_my_body(my_body, my_head, is_move_safe):
  for body in my_body:
    if body["x"] == my_head["x"] + 1 and body["y"] == my_head["y"]:
      is_move_safe["right"] = False
    elif body["x"] == my_head["x"] - 1 and body["y"] == my_head["y"]:
      is_move_safe["left"] = False
    elif body["x"] == my_head["x"] and body["y"] == my_head["y"] + 1:
      is_move_safe["up"] = False
    elif body["x"] == my_head["x"] and body["y"] == my_head["y"] - 1:
      is_move_safe["down"] = False
  return is_move_safe


def is_opponent_body(opponents, my_head, is_move_safe):
  for opponent in opponents:
    for body in opponent["body"]:
      if body["x"] == my_head["x"] + 1 and body["y"] == my_head["y"]:
        is_move_safe["right"] = False
      elif body["x"] == my_head["x"] - 1 and body["y"] == my_head["y"]:
        is_move_safe["left"] = False
      elif body["x"] == my_head["x"] and body["y"] == my_head["y"] + 1:
        is_move_safe["up"] = False
      elif body["x"] == my_head["x"] and body["y"] == my_head["y"] - 1:
        is_move_safe["down"] = False
  return is_move_safe


def is_food(food, my_head):
  possible_food = []
  for f in food:
    if f["x"] == my_head["x"] + 1 and f["y"] == my_head["y"]:
      possible_food.append("right")
    elif f["x"] == my_head["x"] - 1 and f["y"] == my_head["y"]:
      possible_food.append("left")
    elif f["x"] == my_head["x"] and f["y"] == my_head["y"] + 1:
      possible_food.append("up")
    elif f["x"] == my_head["x"] and f["y"] == my_head["y"] - 1:
      possible_food.append("down")
  return possible_food
