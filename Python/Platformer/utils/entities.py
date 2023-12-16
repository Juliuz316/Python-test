import pygame
import sys
from Python.Platformer.utils.utilities import import_image


class PhysicsEntity:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y

        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False
        self.inAir = True

        self.vel = 3
        self.maxYspeed = 3

        self.image = import_image(self, path)
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if self.inAir == True:
            self.y += 1

