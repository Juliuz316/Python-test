import pygame
import sys
from Python.Platformer.utils.utilities import import_image, import_images


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

        self.idle_animation = import_images("entities/player/idle")

        self.image = import_image("entities/player.png")
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self, window):
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
        if self.inAir:
            self.y += 1
        if not self.movingUp and not self.movingDown and not self.movingRight and not self.movingLeft:
            for anim_index in range(len(self.idle_animation) - 1):
                self.image = self.idle_animation[anim_index]

