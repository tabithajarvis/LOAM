import pygame
import environment


class Item:
    def __init__(self):
        self.width = environment.TileWidth
        self.height = environment.TileHeight
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((225, 25, 225))