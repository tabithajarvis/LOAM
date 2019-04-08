import environment
import pygame
from tile import Tile

class Map:
    def __init__(self, surface):
        self.map_surface = pygame.Surface((environment.ScreenHeight, environment.ScreenWidth))
        self.tilemap = []
        for i in range(0, environment.MapHeight):
            row = []
            for j in range(0, environment.MapWidth):
                row.append(Tile(surface.get_at((i, j))))
            self.tilemap.append(row)

    def draw(self):
        for i in range(0, environment.MapHeight):
            row = self.tilemap[i]
            for j in range(0, environment.MapWidth):
                pygame.draw.rect(self.map_surface, row[j].color, (i*environment.TileWidth, j*environment.TileHeight, environment.TileWidth, environment.TileHeight), 0)
