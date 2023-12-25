import pygame

BASE_PATH = "data/"


def import_image(path):
    img = pygame.image.load(BASE_PATH + path)
    return img


def game_over(screen, score):
    text_font1 = pygame.font.Font("freesansbold.ttf", 80)
    text_font2 = pygame.font.Font("freesansbold.ttf", 40)
    game_over_text = text_font1.render("GAME OVER", False, (255, 255, 255))
    game_over_score = text_font2.render("Your score is: " + str(score), False, (255, 255, 255))
    screen.blit(game_over_text, (200, 250))
    screen.blit(game_over_score, (200, 150))
