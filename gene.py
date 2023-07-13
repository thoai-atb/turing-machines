import random


class Gene:
  # Directions
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

  # Code indices
  VALUE = 0
  DIRECTION = 1
  NEXT_STATE = 2

  def __init__(self, num_states: int):
    self.num_states = num_states  # number of states
    self.code = []
    self.generate_code()
    print(self.code)

  def __str__(self):
    return str(self.code)

  def generate_code(self):
    code = []
    for _ in range(self.num_states):
      state_code = []
      for _ in range(2):
        state_code.append(
          (
            random.choice([0, 1]), 
            random.choice(
              [Gene.UP, Gene.DOWN, Gene.LEFT, Gene.RIGHT]
            ),
            random.randint(0, self.num_states - 1)
          )
        )
      code.append(state_code)
    self.code = code
  
  def get_value(self, state: int, value: int):
    return self.code[state][value][Gene.VALUE]

  def get_direction(self, state: int, value: int):
    return self.code[state][value][Gene.DIRECTION]

  def get_next_state(self, state: int, value: int):
    return self.code[state][value][Gene.NEXT_STATE]
        
