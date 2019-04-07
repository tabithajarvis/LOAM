import pygame
from menu import Menu

class Environment:
    ScreenWidth = 1280
    ScreenHeight = 960
    TileWidth = 32
    TileHeight = 32

def main():
    pygame.init()

    pygame.display.set_caption("LOAM")

    screen = pygame.display.set_mode((Environment.ScreenWidth, Environment.ScreenHeight))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__=="__main__":
    main()
