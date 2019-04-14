import pygame
import environment
from node import a_star
from moveable import Moveable
from moveable import Direction


class Pawn(Moveable):
    def __init__(self, x, y):
        self.width = environment.TileWidth
        self.height = environment.TileHeight
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((225, 25, 225))
        self.x = x
        self.y = y
        self.pathmap = self.pathmap_init()
        self.vision_range = 5
        self.current_path = []

    def pathmap_init(self):
        pathmap = []
        for i in range(0, environment.MapHeight):
            pathrow = []
            for j in range(0, environment.MapWidth):
                    pathrow.append(1.0)
            pathmap.append(pathrow)
        return pathmap

    def path_find(self, target_position):
        self.current_path = a_star(self.pathmap, (self.x, self.y), target_position)

    def path_follow(self):
        if self.current_path:
            if self.current_path[0][1] > self.y:
                self.move(Direction.DOWN)
            elif self.current_path[0][1] < self.y:
                self.move(Direction.UP)
            if self.current_path[0][0] < self.x:
                self.move(Direction.LEFT)
            elif self.current_path[0][0] > self.x:
                self.move(Direction.RIGHT)
            self.current_path.pop(0)

    def vision_check(self, current_map):
        change = False
        for i in range(self.vision_range*2 + 1):
            for j in range(self.vision_range*2 + 1):
                if self.pathmap[i+self.x-self.vision_range][j+self.y-self.vision_range] != current_map[i+self.x-self.vision_range][j+self.y-self.vision_range]:
                    self.pathmap[i+self.x-self.vision_range][j+self.y-self.vision_range] = current_map[i+self.x-self.vision_range][j+self.y-self.vision_range]
                    change = True
        return change


    def update(self, current_pathmap):
        if self.vision_check(current_pathmap):
            self.path_find(self.current_path[-1])
        self.path_follow()



#   def map_merge(self, pathmap):
#      if len(pathmap) == len(self.pathmap) & len(pathmap[0]) == len(self.pathmap[0]):
#           for i in range(len(pathmap)):
#               for j in range(len(pathmap[0])):


