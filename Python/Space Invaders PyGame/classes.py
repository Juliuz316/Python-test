import pygame


class Entity:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.speed = speed

        self.movement = {"left": False, "right": False}

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def alien_movement(self):
        if self.x < 800 - self.image.get_width() and self.movement["right"]:
            self.x += self.speed
        elif self.rect.right >= 799:
            self.movement["right"] = False
            self.y += 20
            self.x -= self.speed
            self.movement["left"] = True
        elif self.x > 0 and self.movement["left"]:
            self.x -= self.speed
        elif self.rect.left <= 1:
            self.movement["left"] = False
            self.y += 20
            self.x += self.speed
            self.movement["right"] = True



class Projectile:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.speed = -5

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        self.rect.x = self.x


class Score:
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y
        self.score_val = 0
        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.score_label = 0

    def update(self, screen):
        self.score_label = self.font.render("Score: " + str(self.score_val), False, (255, 255, 255))
        screen.blit(self.score_label, (self.x, self.y))
