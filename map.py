import environment
import pygame
from tile import Tile

# Returns a surface with the path passed in drawn
def path_overlay(path):
    path_color = pygame.Color(0, 255, 0, 127)
    surface = pygame.Surface((environment.ScreenWidth, environment.ScreenHeight), flags=pygame.SRCALPHA)
    for node in path:
        pygame.draw.rect(surface, path_color, (node[0]*environment.TileWidth, node[1]*environment.TileHeight, environment.TileWidth, environment.TileHeight), 0)
    return surface

# Returns a surface with a grid for the entire screen view
def grid_overlay():
    grid_color = pygame.Color(0, 0, 0, 100)
    surface = pygame.Surface((environment.ScreenWidth, environment.ScreenHeight), flags=pygame.SRCALPHA)
    for i in range(0, environment.ScreenWidth, environment.TileWidth):
        pygame.draw.line(surface, grid_color, (i, 0), (i, environment.ScreenHeight))
    for i in range(0, environment.ScreenHeight, environment.TileHeight):
        pygame.draw.line(surface, grid_color, (0, i), (environment.ScreenWidth, i))
    return surface

# Returns a surface with a vision overlay for a passed in Pawn
def vision_overlay(person):
    vision_color = pygame.Color(0, 255, 255, 127)
    surface = pygame.Surface((environment.ScreenWidth, environment.ScreenHeight), flags=pygame.SRCALPHA)
    pygame.draw.rect(
        surface, vision_color,
            (person.min_view()[0]*environment.TileWidth,
             person.min_view()[1]*environment.TileHeight,
             (person.max_view()[0] - person.min_view()[0] + 1)*environment.TileWidth,
             (person.max_view()[1] - person.min_view()[1] + 1)*environment.TileHeight),
             0)
    return surface

class Map:
    def __init__(self, surface):
        self.map_surface = pygame.Surface((environment.ScreenWidth, environment.ScreenHeight))
        self.tilemap = []
        self.pathmap = []
        for i in range(0, environment.MapHeight):
            row = []
            pathrow = []
            for j in range(0, environment.MapWidth):
                row.append(Tile(surface.get_at((j, i))))
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
                pygame.draw.rect(self.map_surface, row[j].color, (j*environment.TileWidth, i*environment.TileHeight, environment.TileWidth, environment.TileHeight), 0)
