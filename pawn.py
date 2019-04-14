import pygame
import environment
from path import a_star, create_pathmap
from moveable import Moveable, Direction


class Pawn(Moveable):
    def __init__(self, x, y):
        self.width = environment.TileWidth
        self.height = environment.TileHeight
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((225, 25, 225))
        self.x = x
        self.y = y
        self.pathmap = create_pathmap(environment.MapWidth, environment.MapHeight, fill=1.0)
        self.vision_range = 10
        self.current_path = []
        self.set_target((self.x, self.y))

    def path_find(self):
        self.current_path = a_star(self.pathmap, (self.x, self.y), self.target)

    def path_follow(self):
        if self.current_path:
            move_to = self.current_path.pop()
            if move_to[1] > self.y:
                self.move(Direction.DOWN)
            elif move_to[1] < self.y:
                self.move(Direction.UP)
            elif move_to[0] < self.x:
                self.move(Direction.LEFT)
            elif move_to[0] > self.x:
                self.move(Direction.RIGHT)

    def set_target(self, position):
        self.target = position
        self.path_find()

    def vision_check(self, current_map):
        change = False

        min_view_x = max(self.x - self.vision_range, 0)
        max_view_x = min(self.x + self.vision_range, len(current_map[0]) - 1)
        min_view_y = max(self.y - self.vision_range, 0)
        max_view_y = min(self.y + self.vision_range, len(current_map) - 1)

        for i in range(min_view_y, max_view_y + 1):
            for j in range(min_view_x, max_view_x + 1):
                if self.pathmap[min_view_y + i][min_view_x + j] != current_map[min_view_y + i][min_view_x + j]:
                    self.pathmap[min_view_y + i][min_view_x + j] = current_map[min_view_y + i][min_view_x + j]
                    change = True
        return change


    def update(self, current_pathmap):
        if self.vision_check(current_pathmap):
            self.path_find()
        self.path_follow()



#   def map_merge(self, pathmap):
#      if len(pathmap) == len(self.pathmap) & len(pathmap[0]) == len(self.pathmap[0]):
#           for i in range(len(pathmap)):
#               for j in range(len(pathmap[0])):
