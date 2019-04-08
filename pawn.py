import pygame
import random
import environment


class Pawn:
    def __init__(self, x, y):
        self.width = environment.TileWidth
        self.height = environment.TileHeight
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((225, 25, 225))
        self.x = x
        self.y = y

    def move_randomly(self):
        direction = random.randint(0, 4)
        if direction == 1:
            self.x = max(self.x - 1, 0)
        elif direction == 2:
            self.x = min(self.x + 1, environment.MapWidth - 1)
        elif direction == 3:
            self.y = max(self.y - 1, 0)
        elif direction == 4:
            self.y = min(self.y + 1, environment.MapHeight - 1)
        else:
            "That webpage is a liar."
