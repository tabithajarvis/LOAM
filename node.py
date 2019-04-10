#Node for pathfinding and decision making using A*
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.distance = 0
        self.heuristic = 0
        self.cost = 0

    def __eq__(self, other):
        return self.position == other.position
