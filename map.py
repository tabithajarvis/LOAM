import environment
from enum import IntEnum
import pygame


class TileType(IntEnum):
    GRASS = 0
    WALL = 1
    DOOR = 2
    FLOOR = 3
    FARMLAND = 4


class Tile:
    def __init__(self, color):
        if color == pygame.Color(34, 177, 76, 255):
            self.type = TileType.GRASS
        elif color == pygame.Color(185, 122, 87, 255):
            self.type = TileType.WALL
        elif color == pygame.Color(255, 201, 14, 255):
            self.type = TileType.DOOR
        elif color == pygame.Color(195, 195, 195, 255):
            self.type = TileType.FLOOR
        elif color == pygame.Color(181, 230, 29, 255):
            self.type = TileType.FARMLAND
        else:
            print("Tile color not mapped!")

class Map:
    def __init__(self, surface):
        self.tilemap = []
        for i in range(0, environment.MapHeight):
            row = []
            for j in range(0, environment.MapWidth):
                row.append(Tile(surface.get_at((i, j))))
            self.tilemap.append(row)
