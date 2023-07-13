from grid import *
from gene import *


class TuringMachine:
    def __init__(self, x: int, y: int, num_states: int):
        self.x = x
        self.y = y
        self.state = 0
        self.gene = Gene(num_states)
        self.states_reached = 0
        self.reached_states = []

    def update(self, grid: Grid, value_code: int = 1):
        ''' value_code is to distinguish between different beavers (greater than 0) '''
        # print("state is : ", self.state)
        value_read = grid.read_value(self.x, self.y)
        if value_read != 0:
            value_read = 1
        # print("value read is: ", value_read)
        next_value = self.gene.get_value(self.state, value_read)
        # print("next value is: ", next_value)
        direction = self.gene.get_direction(self.state, value_read)
        # print("direction is: ", direction)
        new_state = self.gene.get_next_state(self.state, value_read)
        # print("new state is: ", new_state)

        # WRITE
        grid.write_value(self.x, self.y, next_value * value_code)

        # MOVE
        if direction == Gene.UP:
            self.y -= 1
            if self.y < 0:
                self.y = grid.row_count - 1
        elif direction == Gene.DOWN:
            self.y += 1
            if self.y > grid.row_count - 1:
                self.y = 0
        elif direction == Gene.LEFT:
            self.x -= 1
            if self.x < 0:
                self.x = grid.column_count - 1
        elif direction == Gene.RIGHT:
            self.x += 1
            if self.x > grid.column_count - 1:
                self.x = 0

        # UPDATE STATE
        self.state = new_state
        if self.state not in self.reached_states:
            self.reached_states.append(self.state)
            self.states_reached += 1
            # print(f"states reached: {self.states_reached}/{self.gene.num_states}")
