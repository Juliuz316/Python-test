import sys
import pygame

from Python.Platformer.utils.tiles import Tile
from utils.entities import PhysicsEntity


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Platformer")
        self.window = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

        self.hero = PhysicsEntity(100, 100, '\\entities\\player.png')
        self.grass = Tile(100, 200, '\\tiles\\grass\\1.png')

    def run(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.hero.movingUp = True
                    if event.key == pygame.K_DOWN:
                        self.hero.movingDown = True
                    if event.key == pygame.K_LEFT:
                        self.hero.movingLeft = True
                    if event.key == pygame.K_RIGHT:
                        self.hero.movingRight = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.hero.inAir = True
                        self.hero.movingUp = False
                    if event.key == pygame.K_DOWN:
                        self.hero.movingDown = False
                    if event.key == pygame.K_LEFT:
                        self.hero.movingLeft = False
                    if event.key == pygame.K_RIGHT:
                        self.hero.movingRight = False

            if self.hero.movingUp:
                self.hero.y -= self.hero.vel
            if self.hero.movingDown:
                self.hero.y += self.hero.vel
            if self.hero.movingLeft:
                self.hero.x -= self.hero.vel
            if self.hero.movingRight:
                self.hero.x += self.hero.vel

            self.window.fill((10, 220, 240))

            if self.hero.rect.colliderect(self.grass.rect):
                self.hero.inAir = False

            self.window.blit(self.grass.image, (self.grass.x, self.grass.y))
            self.window.blit(self.hero.image, (self.hero.x, self.hero.y))

            self.hero.update()
            self.grass.update()
            self.clock.tick(60)
            pygame.display.update()


Game().run()
