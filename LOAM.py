import pygame
from map import Map
from menu import Menu
import environment

def main():
    pygame.init()

    pygame.display.set_caption("LOAM")

    screen = pygame.display.set_mode((environment.ScreenWidth, environment.ScreenHeight))

    village_map = Map(pygame.image.load("maps/village.png"))

    last_update = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if pygame.time.get_ticks() - last_update  >= environment.refresh_rate:
            village_map.draw()

        screen.blit(village_map.map_surface, (0, 0))
        pygame.display.flip()

if __name__=="__main__":
    main()
