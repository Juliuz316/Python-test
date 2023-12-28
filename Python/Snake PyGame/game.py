import pygame
import sys
from pygame.math import Vector2
from globals import CELL_SIZE, CELL_NUMBER
from entities import Apple, Snake, Score

pygame.init()

# PyGame window settings
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
clock = pygame.time.Clock()
score = 0

# Screen update timer
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 200)


class Game:
    def __init__(self):
        self.apple = Apple()
        self.snake = Snake()
        self.score = Score()

    def draw_snake(self):
        for index, block in enumerate(self.snake.body):
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)

            if index == 0:  # Drawing head by direction

                if self.snake.direction == Vector2(0, -1):
                    screen.blit(self.snake.head_up, (x_pos, y_pos))
                elif self.snake.direction == Vector2(0, 1):
                    screen.blit(self.snake.head_down, (x_pos, y_pos))
                elif self.snake.direction == Vector2(-1, 0):
                    screen.blit(self.snake.head_left, (x_pos, y_pos))
                elif self.snake.direction == Vector2(1, 0) or self.snake.direction == Vector2(0, 0):
                    screen.blit(self.snake.head_right, (x_pos, y_pos))

            elif index == len(self.snake.body) - 1:  # Drawing tail by direction
                previous_block = self.snake.body[-2]
                if previous_block.x == self.snake.body[index].x and previous_block.y < self.snake.body[index].y:
                    screen.blit(self.snake.tail_down, (x_pos, y_pos))
                elif previous_block.x == self.snake.body[index].x and previous_block.y > self.snake.body[index].y:
                    screen.blit(self.snake.tail_up, (x_pos, y_pos))
                elif previous_block.x < self.snake.body[index].x and previous_block.y == self.snake.body[index].y:
                    screen.blit(self.snake.tail_right, (x_pos, y_pos))
                elif previous_block.x > self.snake.body[index].x and previous_block.y == self.snake.body[index].y:
                    screen.blit(self.snake.tail_left, (x_pos, y_pos))

            else:  # Drawing body parts
                previous_block = self.snake.body[index - 1]
                next_block = self.snake.body[index + 1]

                if previous_block.x == self.snake.body[index].x and next_block.y != self.snake.body[index].y:
                    screen.blit(self.snake.body_vertical, (x_pos, y_pos))
                elif previous_block.x != self.snake.body[index].x and next_block.y == self.snake.body[index].y:
                    screen.blit(self.snake.body_horizontal, (x_pos, y_pos))
                elif previous_block == self.snake.body[index] + (0, -1) and next_block == self.snake.body[index] + (-1, 0) or previous_block == self.snake.body[index] + (-1, 0) and next_block == self.snake.body[index] + (0, -1):  # Top left
                    screen.blit(self.snake.body_tl, (x_pos, y_pos))
                elif previous_block == self.snake.body[index] + (0, -1) and next_block == self.snake.body[index] + (1, 0) or previous_block == self.snake.body[index] + (1, 0) and next_block == self.snake.body[index] + (0, -1):  # Top right
                    screen.blit(self.snake.body_tr, (x_pos, y_pos))
                elif previous_block == self.snake.body[index] + (0, 1) and next_block == self.snake.body[index] + (-1, 0) or previous_block == self.snake.body[index] + (-1, 0) and next_block == self.snake.body[index] + (0, 1):  # Bottom left
                    screen.blit(self.snake.body_bl, (x_pos, y_pos))
                elif previous_block == self.snake.body[index] + (1, 0) and next_block == self.snake.body[index] + (0, 1) or previous_block == self.snake.body[index] + (0, 1) and next_block == self.snake.body[index] + (1, 0):  # Bottom right
                    screen.blit(self.snake.body_br, (x_pos, y_pos))

    def draw_apple(self):
        screen.blit(self.apple.image, (self.apple.pos.x, self.apple.pos.y))

    def check_collision(self):
        if self.snake.body[0] == Vector2(self.apple.x, self.apple.y):
            self.apple.randomize(self.snake)
            self.snake.grow()
            self.score.score += 1
            pygame.mixer.Sound("Sound/crunch.wav").play().set_volume(0.4)

        for index, part in enumerate(self.snake.body):
            if index != 0:
                if self.snake.body[0] == self.snake.body[index]:
                    self.game_over()

    def check_borders(self):
        if not 0 <= self.snake.body[0][0] < CELL_NUMBER or not 0 <= self.snake.body[0][1] < CELL_NUMBER:
            game.game_over()

    def game_over(self):
        self.score.save_highscore()
        pygame.quit()
        sys.exit()

    def draw_background(self):
        screen.fill((0, 170, 0))
        for row in range(CELL_NUMBER):
            for col in range(CELL_NUMBER):
                color = (0, 140, 0) if (row + col) % 2 == 0 else (0, 170, 0)
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

    def draw_score(self):
        text = self.score.font.render("Score: " + str(self.score.score), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (CELL_SIZE * CELL_NUMBER - CELL_SIZE, CELL_SIZE * CELL_NUMBER - CELL_SIZE // 2)
        screen.blit(text, text_rect)

    def draw_highscore(self):
        text = self.score.font.render("Highscore: " + str(self.score.load_highscore()), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (CELL_SIZE * 3 - CELL_SIZE, CELL_SIZE * CELL_NUMBER - CELL_SIZE // 2)
        screen.blit(text, text_rect)



game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.game_over()

        if event.type == SCREEN_UPDATE:  # Game update (every 200 ms)
            game.draw_background()
            game.snake.move()
            game.draw_snake()
            game.check_collision()
            game.check_borders()
            game.draw_apple()
            game.draw_score()
            game.draw_highscore()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction != (0, 1):
                    game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if game.snake.direction != (0, -1):
                    game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if game.snake.direction != (1, 0):
                    game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if game.snake.direction != (-1, 0):
                    game.snake.direction = Vector2(1, 0)

    clock.tick(60)
    pygame.display.update()
