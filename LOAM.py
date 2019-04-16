import pygame
from map import Map, path_overlay, grid_overlay, vision_overlay
import environment
from pawn import Pawn
from item import Item

def main():
    pygame.init()

    pygame.display.set_caption("LOAM")

    screen = pygame.display.set_mode((environment.ScreenWidth, environment.ScreenHeight))

    village_map = Map(pygame.image.load("maps/village.png"))

    last_update = pygame.time.get_ticks()

    person = Pawn(30, 30)
    person.set_target((91,6))
    cabbage = Item(60, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if pygame.time.get_ticks() - last_update >= environment.refresh_rate:
            village_map.draw()
            person.update(village_map.pathmap)

            screen.blit(village_map.map_surface, (0, 0))
            screen.blit(person.image, (person.x*environment.TileWidth, person.y*environment.TileHeight))
            screen.blit(path_overlay(person.current_path), (0, 0))
            screen.blit(grid_overlay(), (0, 0))
            screen.blit(vision_overlay(person), (0,0))
            #screen.blit(cabbage.image, (cabbage.x*environment.TileWidth, cabbage.y*environment.TileHeight))
            pygame.display.flip()
            last_update = pygame.time.get_ticks()


if __name__=="__main__":
    main()
