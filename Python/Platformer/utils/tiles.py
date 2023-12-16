import pygame
import sys
from Python.Platformer.utils.utilities import import_image


class Tile:
    def __init__(self, x, y, path):
        self.x = x
        self.y = y

        self.image = import_image(self, path)
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())
