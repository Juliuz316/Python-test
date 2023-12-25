import pygame
import os

SCALE = 2
DEFAULT_PATH = "data/images/"


def import_image(path):
    image = pygame.image.load(DEFAULT_PATH + path)
    image = pygame.transform.scale(image,(image.get_width() * SCALE,image.get_height() * SCALE))
    image.set_colorkey((0, 0, 0))
    return image


def import_images(path):
    images = []
    for img_name in sorted(os.listdir(DEFAULT_PATH + path)):
        images.append(import_image(path + '/' + img_name))
    return images