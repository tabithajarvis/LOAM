import environment
from enum import IntEnum

class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class Moveable:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        if direction == Direction.UP:
            self.y = max(self.y - 1, 0)
        elif direction == Direction.DOWN:
            self.y = min(self.y + 1, environment.MapHeight - 1)
        elif direction == Direction.LEFT:
            self.x = max(self.x - 1, 0)
        else:
            self.x = min(self.x + 1, environment.MapWidth - 1)
