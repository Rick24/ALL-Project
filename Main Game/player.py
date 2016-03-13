from random import randint

import map
import math
import pygame
from image_loader import load_image

CENTER_X = -1
CENTER_Y = -1
FULLXTILE = 48
FULLYTILE = 39
HALFXTILE = 24
HALFYTILE = 19

#Rotate car.
def rot_center(image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect

def findspawn():
    x = 580
    y = 890

    return x, y

#define car as Player.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('player.png')
        self.rect = self.image.get_rect()
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        x, y = findspawn()
        self.x = x
        self.y = y
        self.rect.topleft = self.x, self.y
        self.x, self.y = findspawn()
        self.dir = 0
        self.speed = 0.0
        self.maxspeed = 21.5
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60



#Accelerate the vehicle
    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed = self.speed + self.acceleration
            if self.speed < self.maxspeed / 3:
                self.emit_tracks()

#Deaccelerate.
    def deaccelerate(self):
        if self.speed > self.minspeed:
            self.speed = self.speed - self.deacceleration
            self.emit_tracks()

#Steer.
    def steerleft(self):
        self.dir = self.dir+self.steering
        if self.dir > 360:
            self.dir = 0
        if (self.speed > self.maxspeed / 2):
            self.emit_tracks()
        self.image, self.rect = rot_center(self.image_orig, self.rect, self.dir)

    def moveleft(self):
        self.x =- 10
    def moveright(self):
        self.x =+ 10
    def moveup(self):
        self.y =- 10
    def movedown(self):
        self.y =+ 10
#fix this function
    def update(self, last_x, last_y):
        self.x = self.x + self.speed * math.cos(math.radians(270-self.dir))
        self.y = self.y + self.speed * math.sin(math.radians(270-self.dir))


