
import sys, pygame
from pygame.locals import *

from image_loader import load_image

import map, camera, player

def main():
    quit = False
    cam = camera.Camera()
    character = player.Player()



    map1 = pygame.sprite.Group()
    player1 = pygame.sprite.Group()

    for tile_num in range (0, len(map.map_tiles)):
        map.map_files.append(load_image(map.map_tiles[tile_num], False))
    for x in range (0, 25):
        for y in range (0, 25):
            map1.add(map.Map(map.map_1[x][y], x * 38, y * 49))


    player1.add(character)

    cam.set_pos(0, 0)


    while not quit:
        window.blit(background, (0,0))


        map1.update(cam.x, cam.y)
        map1.draw(window)


        player1.update(cam.x, cam.y)
        player1.draw(window)

        pygame.display.flip()

        for et in pygame.event.get():

            if et.type == pygame.KEYDOWN:
                if (et.key == pygame.K_ESCAPE):
                    quit = True
            elif (et.type == pygame.QUIT):
                quit = True


pygame.init()

window = pygame.display.set_mode((1525,
                                  950),
                                )

font = pygame.font.Font(None, 24)

CENTER_W =  int(pygame.display.Info().current_w /2)
CENTER_H =  int(pygame.display.Info().current_h /2)

#new background surface
background = pygame.Surface(window.get_size())
background = background.convert_alpha()
background.fill((26, 26, 26))

#Enter the mainloop.
main()

pygame.quit()
sys.exit(0)