import pygame
from map import Map
from menu import Menu
import environment

def main():
    pygame.init()

    pygame.display.set_caption("LOAM")

    screen = pygame.display.set_mode((environment.ScreenWidth, environment.ScreenHeight))

    village_map = Map(pygame.image.load("maps/village.png"))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__=="__main__":
    main()
