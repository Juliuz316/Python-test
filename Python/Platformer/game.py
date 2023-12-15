import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.clock.tick(60)
            pygame.display.update()


Game().run()