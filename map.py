import environment
import pygame
from tile import Tile

class Map:
    def __init__(self, surface):
        self.map_surface = pygame.Surface((environment.ScreenHeight, environment.ScreenWidth))
        self.tilemap = []
        self.pathmap = []
        for i in range(0, environment.MapHeight):
            row = []
            pathrow = []
            for j in range(0, environment.MapWidth):
                row.append(Tile(surface.get_at((i, j))))
                if not row[j].passable:
                    # Terrain difficulty is on a (0,inf) scale, where 0 cannot
                    # be attained, as that would be teleportation. So, use 0 as
                    # the 'impassable' value
                    pathrow.append(0)
                else:
                    pathrow.append(1.0)

            self.tilemap.append(row)
            self.pathmap.append(pathrow)

    def draw(self):
        for i in range(0, environment.MapHeight):
            row = self.tilemap[i]
            for j in range(0, environment.MapWidth):
                pygame.draw.rect(self.map_surface, row[j].color, (i*environment.TileWidth, j*environment.TileHeight, environment.TileWidth, environment.TileHeight), 0)
