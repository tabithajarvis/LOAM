import math

HeuristicMultiplier = 2

# Node for pathfinding and decision making using A*
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.distance = 0
        self.heuristic = 0
        self.difficulty = 0

    def cost(self):
        return self.distance + self.heuristic

    def __eq__(self, other):
        return self.position == other.position

# Creates a pathmap
def create_pathmap(width, height, fill=1.0):
    pathmap = []
    for i in range(0, height):
        pathrow = []
        for j in range(0, width):
            pathrow.append(fill)
        pathmap.append(pathrow)
    return pathmap

def a_star(pathmap, start, goal):
    start_node = Node(None, start)
    end_node = Node(None, goal)

    # All nodes get added (as they are encountered) to the open list, and then
    # moved to the closed list when 'visited'. When moving to a new node and
    # adding it to the closed list, we then add the newly encountered nodes
    # around that one to the open list.
    open_list = []
    closed_list = []
    column_bound = len(pathmap) - 1
    row_bound = len(pathmap[0]) - 1

    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.cost() < current_node.cost():
                current_node = item
                current_index = index

        closed_list.append(open_list.pop(current_index))

        # We have reached the end- return the path
        if current_node == end_node:
            path = []
            traceback_node = current_node
            while traceback_node is not None:
                path.append(traceback_node.position)
                traceback_node = traceback_node.parent
            return path

        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # Adjacent squares
            # Get next node position
            next_node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # If not within range (edges), continue
            if next_node_position[0] > row_bound or next_node_position[0] < 0 or \
                    next_node_position[1] > column_bound or next_node_position[1] < 0:
                continue

            difficulty = pathmap[next_node_position[0]][next_node_position[1]]

            # Make sure terrain is passable
            if difficulty == 0:
                continue

            new_node = Node(current_node, next_node_position)

            # If the node is already on the closed listed, continue
            node_found = False
            for node in closed_list:
                if new_node == node:
                    node_found = True
                    break
            if node_found:
                continue

            # Fill the node
            new_node.difficulty = difficulty
            new_node.distance = current_node.distance + difficulty
            new_node.heuristic = (abs(new_node.position[0] - end_node.position[0]) +
                        abs(new_node.position[1] - end_node.position[1])) * HeuristicMultiplier

            # The node is already in the open list, but cheaper. Continue.
            for open_node in open_list:
                if new_node == open_node and new_node.distance > open_node.distance:
                    continue

            # Add the child to the open list
            open_list.append(new_node)
