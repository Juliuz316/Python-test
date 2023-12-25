import pygame
import sys
import random
from utils import import_image, game_over
from classes import Entity, Projectile, Score


# Initialize PyGame
pygame.init()

# Display settings
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Image import
assets = {
    "ship": import_image("spaceship.png"),
    "projectile": import_image("bullet.png"),
    "alien": import_image("alien.png"),
}

# Initialize objects
player = Entity(screen.get_width()/2 - 32, screen.get_height() * 0.8, assets["ship"], 5)
projectile_rendered = False
projectile = Projectile(player.x + player.image.get_width() / 2 - 16,
                        player.y - player.image.get_height() + 32, assets["projectile"])
projectiles = []
aliens = []
score = Score()

# Add initial aliens
for i in range(4):
    aliens.append(Entity(random.randint(50, 400), random.randint(100, 300), assets["alien"], 2))
    aliens[i].movement["right"] = True

# Start BGM

pygame.mixer.Sound("data/background.wav").play().set_volume(0.1)

# Game loop
over = False
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.movement["left"] = True
            if event.key == pygame.K_RIGHT:
                player.movement["right"] = True
            if event.key == pygame.K_SPACE:
                if not projectile_rendered:
                    projectile_rendered = True
                    projectile = Projectile(player.x + player.image.get_width() / 2 - 16,
                                            player.y - player.image.get_height() + 32, assets["projectile"])
                    pygame.mixer.Sound("data/bullet.wav").play().set_volume(0.4)
                    projectiles.append(projectile)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.movement["left"] = False
            if event.key == pygame.K_RIGHT:
                player.movement["right"] = False

    # Move while button is being held down
    if player.movement["left"]:
        player.x -= player.speed
    if player.movement["right"]:
        player.x += player.speed

    # Movement boundaries
    if player.x > screen.get_width() - player.image.get_width():
        player.x = screen.get_width() - player.image.get_width()
    if player.x < 0:
        player.x = 0

    # Check for collisions
    for i in aliens:
        for ii in projectiles:
            if i.rect.colliderect(ii.rect):
                aliens.remove(i)
                projectiles.remove(ii)
                pygame.mixer.Sound("data/explosion.wav").play().set_volume(0.4)
                score.score_val += 1
                projectile_rendered = False
                aliens.append(Entity(random.randint(50, 400), random.randint(100, 300), assets["alien"], 2))
                break

    # Update positions of entities
    screen.blit(player.image, (player.x, player.y))
    if len(aliens) > 0:
        for alien in aliens:
            screen.blit(alien.image, (alien.x, alien.y))
            alien.alien_movement()
            alien.update()

    player.update()

    for projectile in projectiles:
        projectile.update()
        screen.blit(projectile.image, (projectile.x, projectile.y))
        if projectile.y < -32:
            projectiles.remove(projectile)
            projectile_rendered = False

    # Game over
    for alien in aliens:
        if alien.y >= 375:
            pygame.mixer.Sound("data/explosion.wav").play().set_volume(0.4)
            over = True

    if over:
        aliens.clear()
        game_over(screen, score.score_val)
        for event in pygame.event.get():
            if event.key == pygame.K_RETURN:
                pygame.quit()
                sys.exit()

    score.update(screen)

    clock.tick(60)
    pygame.display.update()
