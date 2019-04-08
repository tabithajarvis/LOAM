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
