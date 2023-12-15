import sys
import pygame


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Platformer")
        self.window = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

        self.hero = pygame.image.load("data/images/entities/player.png")
        # self.img = pygame.transform.scale(self.img, (25, 50))
        self.hero.set_colorkey((0, 0, 0))

        self.heroX, self.heroY = 100, 100
        self.vel = 3
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False
        # self.test_collision = pygame.Rect(50, 50, 300, 50)

    def run(self):
        while True:

            hero_collision = pygame.Rect(self.heroX, self.heroY, self.hero.get_width(), self.hero.get_height())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movingUp = True
                    if event.key == pygame.K_DOWN:
                        self.movingDown = True
                    if event.key == pygame.K_LEFT:
                        self.movingLeft = True
                    if event.key == pygame.K_RIGHT:
                        self.movingRight = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movingUp = False
                    if event.key == pygame.K_DOWN:
                        self.movingDown = False
                    if event.key == pygame.K_LEFT:
                        self.movingLeft = False
                    if event.key == pygame.K_RIGHT:
                        self.movingRight = False

            if self.movingUp:
                self.heroY -= self.vel
            if self.movingDown:
                self.heroY += self.vel
            if self.movingLeft:
                self.heroX -= self.vel
            if self.movingRight:
                self.heroX += self.vel

            self.window.fill((10, 220, 240))
            # if hero_collision.colliderect(self.test_collision):
            #     pygame.draw.rect(self.window, (0, 0 ,0), self.test_collision)
            # else:
            #     pygame.draw.rect(self.window, (120, 120, 0), self.test_collision)

            self.window.blit(self.hero, (self.heroX, self.heroY))
            self.clock.tick(60)
            pygame.display.update()


Game().run()
