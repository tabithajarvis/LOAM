import pygame
import environment
from moveable import Moveable


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

    def pathmap_init(self):
        pathmap = []
        for i in range(0, environment.MapHeight):
            pathrow = []
            for j in range(0, environment.MapWidth):
                    pathrow.append(1.0)
            pathmap.append(pathrow)
        return pathmap

#   def map_merge(self, pathmap):
#      if len(pathmap) == len(self.pathmap) & len(pathmap[0]) == len(self.pathmap[0]):
#           for i in range(len(pathmap)):
#               for j in range(len(pathmap[0])):


