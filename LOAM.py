import pygame
from map import Map
from menu import Menu
import environment
from pawn import Pawn
from item import Item
from moveable import Direction
from tile import Tile
from node import Node

def main():
    pygame.init()

    pygame.display.set_caption("LOAM")

    screen = pygame.display.set_mode((environment.ScreenWidth, environment.ScreenHeight))

    village_map = Map(pygame.image.load("maps/village.png"))

    last_update = pygame.time.get_ticks()

    person = Pawn(30, 30)

    cabbage = Item(60, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if pygame.time.get_ticks() - last_update  >= environment.refresh_rate:
            village_map.draw()
            person.move(Direction.RIGHT)
            cabbage.move(Direction.DOWN)

        screen.blit(village_map.map_surface, (0, 0))
        screen.blit(person.image, (person.x*environment.TileWidth, person.y*environment.TileHeight))
        screen.blit(cabbage.image, (cabbage.x*environment.TileWidth, cabbage.y*environment.TileHeight))
        pygame.display.flip()

if __name__=="__main__":
    main()
