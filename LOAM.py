import pygame
from map import Map
from menu import Menu
import environment
from pawn import Pawn
from item import Item
from moveable import Direction
from tile import Tile
from node import Node


def a_star(pathmap, start, goal):

    start_node = Node(None, start)
    end_node = Node(None, goal)

    open_list = []
    closed_list = []

    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.cost < current_node.cost:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Return reversed path

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(pathmap) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(pathmap[len(pathmap) - 1]) - 1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if pathmap[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.distance = current_node.heuristic + 1
            child.heuristic = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.cost = child.distance + child.distance

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.distance > open_node.distance:
                    continue

            # Add the child to the open list
            open_list.append(child)


def main():
    pygame.init()

    pygame.display.set_caption("LOAM")

    screen = pygame.display.set_mode((environment.ScreenWidth, environment.ScreenHeight))

    village_map = Map(pygame.image.load("maps/village.png"))

    last_update = pygame.time.get_ticks()

    person = Pawn(30, 30)

    cabbage = Item(60, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if pygame.time.get_ticks() - last_update  >= environment.refresh_rate:
            village_map.draw()
            person.move(Direction.RIGHT)
            cabbage.move(Direction.DOWN)

        screen.blit(village_map.map_surface, (0, 0))
        screen.blit(person.image, (person.x*environment.TileWidth, person.y*environment.TileHeight))
        screen.blit(cabbage.image, (cabbage.x*environment.TileWidth, cabbage.y*environment.TileHeight))
        pygame.display.flip()

if __name__=="__main__":
    main()
