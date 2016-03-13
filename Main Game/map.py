
import pygame

#Map filenames.

map_files = []
map_tiles = ['floor.png', 'aisle.png', 'start.png']

#Map to tile.
floortile = 0
aisletile = 1
startfinishtile = 2


#tilemap.
map_1 = [
          [0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0], #1
          [0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0], #2
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #3
          [0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0], #4
          [0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0], #5
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #6
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #7
          [0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0], #8
          [0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0], #9
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #10
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #11
          [0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0], #12
          [0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0], #13
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #14
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #15
          [0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0], #16
          [0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0], #17
          [0,0,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0], #18
          [0,0,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0], #19
          [0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0], #20
          [0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0], #21
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #22
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], #23
          [0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0], #24
          [0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0], #25
        ]


class Map(pygame.sprite.Sprite):
    def __init__(self, tile_map, y, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = map_files[tile_map]
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

#Realign the map
    def update(self, cameraX, cameraY):
        self.rect.topleft = self.x - cameraX, self.y - cameraY