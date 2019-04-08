import pygame
from enum import IntEnum

class TileType(IntEnum):
    GRASS = 0
    WALL = 1
    DOOR = 2
    FLOOR = 3
    FARMLAND = 4


class Tile:
    def __init__(self, color):
        self.color = color
        self.passable = True
        if color == pygame.Color(34, 177, 76, 255):
            self.type = TileType.GRASS
        elif color == pygame.Color(185, 122, 87, 255):
            self.type = TileType.WALL
            self.passable = False
        elif color == pygame.Color(255, 201, 14, 255):
            self.type = TileType.DOOR
        elif color == pygame.Color(195, 195, 195, 255):
            self.type = TileType.FLOOR
        elif color == pygame.Color(181, 230, 29, 255):
            self.type = TileType.FARMLAND
        else:
            print("Tile color not mapped!")
