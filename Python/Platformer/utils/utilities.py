import pygame

SCALE = 2
DEFAULT_PATH = "data\images"


def import_image(self, path):
    self.image = pygame.image.load(DEFAULT_PATH + path)
    self.image = pygame.transform.scale(self.image,(self.image.get_width() * SCALE,self.image.get_height() * SCALE))
    self.image.set_colorkey((0, 0, 0))
    return self.image
