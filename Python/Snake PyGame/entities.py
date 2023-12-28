import pygame
import sys
import random
from pygame.math import Vector2
from globals import CELL_SIZE, CELL_NUMBER


class Apple:
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x * CELL_SIZE, self.y * CELL_SIZE)
        self.image = pygame.image.load("Graphics/apple.png").convert_alpha()

    def randomize(self, snake):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x * CELL_SIZE, self.y * CELL_SIZE)
        for block in snake.body:
            if self.pos // CELL_SIZE == block:  # Don't spawn on snake
                self.x = random.randint(0, CELL_NUMBER - 1)
                self.y = random.randint(0, CELL_NUMBER - 1)
                self.pos = Vector2(self.x * CELL_SIZE, self.y * CELL_SIZE)


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.rect = []
        self.direction = Vector2(0, 0)

        self.head_up = pygame.image.load("Graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("Graphics/head_down.png").convert_alpha()
        self.head_left = pygame.image.load("Graphics/head_left.png").convert_alpha()
        self.head_right = pygame.image.load("Graphics/head_right.png").convert_alpha()

        self.tail_up = pygame.image.load("Graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("Graphics/tail_down.png").convert_alpha()
        self.tail_left = pygame.image.load("Graphics/tail_left.png").convert_alpha()
        self.tail_right = pygame.image.load("Graphics/tail_right.png").convert_alpha()

        self.body_vertical = pygame.image.load("Graphics/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()
        self.body_bl = pygame.image.load("Graphics/body_bl.png").convert_alpha()
        self.body_br = pygame.image.load("Graphics/body_br.png").convert_alpha()
        self.body_tl = pygame.image.load("Graphics/body_tl.png").convert_alpha()
        self.body_tr = pygame.image.load("Graphics/body_tr.png").convert_alpha()

    def move(self):
        if self.direction != (0, 0):
            body_copy = self.body[:-1]
            body_copy.insert(0, self.body[0] + self.direction)
            self.body = body_copy

    def grow(self):
        self.body.insert(-1, self.body[-1])


class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font("Font/PoetsenOne-Regular.ttf", 16)

    def save_highscore(self):
        with open("highscore.txt", "a") as f:
            f.write(str(self.score) + "\n")

    def load_highscore(self):
        with open("highscore.txt", "r") as f:
            scores = [int(score.strip()) for score in f.readlines()]
            if len(scores) == 0:
                highscore = 0
            else:
                highscore = max(scores)
            return highscore
