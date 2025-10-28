class Components:

  def __init__(self, game_state):
    self.height = game_state['board']['height']
    self.width = game_state['board']['width']
    self.food = game_state['board']['food']
    self.health = game_state['you']['health']
    self.id = game_state['you']['id']
    self.body = game_state['you']['body']
    self.head = self.body[0]
    self.snakes = game_state['board']['snakes']
    self.turn = game_state['turn']
    self.board = None
